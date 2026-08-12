document.getElementById('predictBtn').addEventListener('click', async () => {
    const income = document.getElementById('income').value;
    const house_age = document.getElementById('house_age').value;
    const rooms = document.getElementById('rooms').value;
    const resultDiv = document.getElementById('result');

    // 1. Basic field validation
    if (!income || !house_age || !rooms) {
        alert('Please fill out all fields before running the evaluation!');
        return;
    }

    // 2. Set UI to Loading status
    resultDiv.style.display = 'block';
    resultDiv.style.backgroundColor = '#edf2f7';
    resultDiv.style.color = '#4a5568';
    resultDiv.style.border = '1px solid #cbd5e0';
    resultDiv.innerText = 'Consulting Kaggle Model...';

    try {
        // 3. Post data payload to your active Flask endpoint
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ income, house_age, rooms }) // Keys match server.py variables exactly!
        });

        const data = await response.json();

        // 4. Handle response and update view
        if (response.ok) {
            resultDiv.style.backgroundColor = '#e6fffa';
            resultDiv.style.color = '#319795';
            resultDiv.style.border = '1px solid #b2f5ea';
            resultDiv.innerHTML = `Estimated Valuation:<br><span style="font-size: 26px; color: #234e52;">${data.estimated_price.toLocaleString('en-IN')}</span>`;
        } else {
            resultDiv.innerText = `Error: ${data.error}`;
        }
    } catch (error) {
        console.error('Network Error:', error);
        resultDiv.style.backgroundColor = '#fff5f5';
        resultDiv.style.color = '#c53030';
        resultDiv.style.border = '1px solid #fed7d7';
        resultDiv.innerText = 'Error: Unable to connect to your local Python server.';
    }
});