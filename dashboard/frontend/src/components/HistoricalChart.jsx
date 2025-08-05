import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from '../api/client';

function HistoricalChart() {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    axios.get('/api/events/price_trend')
      .then(response => {
        const { dates, prices } = response.data;
        setChartData({
          labels: dates,
          datasets: [{
            label: 'Brent Oil Price',
            data: prices,
            fill: false,
            borderColor: 'rgba(75,192,192,1)',
            tension: 0.1
          }]
        });
      });
  }, []);

  if (!chartData) return <p>Loading chart...</p>;

  return (
    <div>
      <h3>📈 Historical Brent Oil Price Trend</h3>
      <Line data={chartData} />
    </div>
  );
}

export default HistoricalChart;
