const socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('alert', function(data) {
    const alertsDiv = document.getElementById('alerts');
    const alertMessage = `
        <p>
            <strong>Suspicious Activity Detected:</strong><br>
            IP: ${data.ip_address} <br>
            Username: ${data.username} <br>
            Time: ${data.timestamp}
        </p>
        <hr>
    `;
    alertsDiv.innerHTML += alertMessage;
});
