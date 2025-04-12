document.addEventListener('DOMContentLoaded', function() {
  const queryInput = document.getElementById('query');
  const calculateButton = document.getElementById('calculate');
  const resultDiv = document.getElementById('result');

  function showLoading() {
    resultDiv.className = 'loading';
    resultDiv.textContent = 'Calculating...';
  }

  function showError(message) {
    resultDiv.className = 'error';
    resultDiv.textContent = `Error: ${message}`;
    console.error('Math Agent Error:', message);
  }

  function showResult(result) {
    resultDiv.className = '';
    resultDiv.textContent = `Result: ${result}`;
    console.log('Math Agent Result:', result);
  }

  calculateButton.addEventListener('click', async function() {
    const query = queryInput.value.trim();
    
    if (!query) {
      showError('Please enter a math query');
      return;
    }

    showLoading();

    try {
      const response = await fetch('http://localhost:5000/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })
      });

      if (!response.ok) {
        throw new Error(`Server responded with status: ${response.status}`);
      }

      const data = await response.json();
      
      if (data.error) {
        showError(data.error);
      } else {
        showResult(data.result);
      }
    } catch (error) {
      showError('Failed to connect to the math agent server. Make sure it\'s running.');
      console.error('Network Error:', error);
    }
  });

  // Enable Enter key to trigger calculation
  queryInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
      calculateButton.click();
    }
  });
});