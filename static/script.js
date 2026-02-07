document.addEventListener('DOMContentLoaded', () => {
    const searchBtn = document.getElementById('searchBtn');
    const flightInput = document.getElementById('flightInput');
    const resultsContainer = document.getElementById('resultsContainer');
    const loading = document.getElementById('loading');
    const errorContainer = document.getElementById('errorContainer');
    const errorMessage = document.getElementById('errorMessage');

    // Add event listener for "Enter" key
    flightInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            searchFlight();
        }
    });

    searchBtn.addEventListener('click', searchFlight);

    async function searchFlight() {
        const flightNumber = flightInput.value.trim();

        if (!flightNumber) {
            showError("Please enter a flight number.");
            return;
        }

        // Reset UI
        resultsContainer.classList.add('hidden');
        errorContainer.classList.add('hidden');
        loading.classList.remove('hidden');

        try {
            const response = await fetch(`/api/flight/${flightNumber}`);
            
            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.error || 'Flight not found');
            }

            const flight = await response.json();
            displayFlight(flight);
        } catch (error) {
            showError(error.message);
        } finally {
            loading.classList.add('hidden');
        }
    }

    function displayFlight(flight) {
        // Extract city codes from location strings (e.g., "New York (JFK)" -> "JFK")
        const startCode = flight.start_location.match(/\((.*?)\)/)?.[1] || flight.start_location;
        const endCode = flight.end_location.match(/\((.*?)\)/)?.[1] || flight.end_location;

        const html = `
            <div class="result-header">
                <span class="flight-number">${flight.flight_number}</span>
                <span class="status" style="color: var(--success); font-weight: 600;"><i class="fas fa-circle" style="font-size: 0.6rem; margin-right: 0.5rem;"></i>On Time</span>
            </div>
            
            <div class="flight-route">
                <div class="route-point">
                    <span class="city-time">${flight.start_time}</span>
                    <span class="city-code">${startCode}</span>
                    <span class="city-zone">${flight.start_location.split('(')[0].trim()} • ${flight.time_zone_start}</span>
                </div>
                
                <div class="route-line">
                    <i class="fas fa-plane plane-icon"></i>
                </div>
                
                <div class="route-point">
                    <span class="city-time">${flight.end_time}</span>
                    <span class="city-code">${endCode}</span>
                    <span class="city-zone">${flight.end_location.split('(')[0].trim()} • ${flight.time_zone_end}</span>
                </div>
            </div>
        `;

        resultsContainer.innerHTML = html;
        resultsContainer.classList.remove('hidden');
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorContainer.classList.remove('hidden');
    }
});
