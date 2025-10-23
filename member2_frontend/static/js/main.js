document.addEventListener('DOMContentLoaded', function() {
    // Handle data form submission
    const dataForm = document.getElementById('dataForm');
    const responseDiv = document.getElementById('response');

    dataForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const dataInput = document.getElementById('dataInput');
        const data = dataInput.value;

        try {
            const response = await fetch('/data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ data: data })
            });

            const result = await response.json();
            
            responseDiv.className = 'show success';
            responseDiv.textContent = `Success! Received: ${result.received || result.message}`;
            
            dataInput.value = '';
        } catch (error) {
            responseDiv.className = 'show error';
            responseDiv.textContent = 'Error submitting data: ' + error.message;
        }
    });

    // Handle health check
    const healthButton = document.getElementById('checkHealth');
    const healthStatus = document.getElementById('healthStatus');

    healthButton.addEventListener('click', async function() {
        try {
            const response = await fetch('/health');
            const result = await response.text();
            
            healthStatus.className = 'show success';
            healthStatus.textContent = `Health Status: ${result}`;
        } catch (error) {
            healthStatus.className = 'show error';
            healthStatus.textContent = 'Error checking health: ' + error.message;
        }
    });
});