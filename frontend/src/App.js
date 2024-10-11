import React, { useState } from 'react';
import axios from 'axios';
import './index.css';

function App() {
  const [animeTitle, setAnimeTitle] = useState('');
  const [recommendations, setRecommendations] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    
    axios.post('http://127.0.0.1:5000/recommend', { anime_title: animeTitle })
      .then(response => {
        setRecommendations(response.data.recommendations);
      })
      .catch(error => {
        console.error('There was an error making the request!', error);
      });
  };

  return (
    <div className="App">
      <h1>Anime Recommendation System</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Enter Anime Title:
          <input
            type="text"
            value={animeTitle}
            onChange={(e) => setAnimeTitle(e.target.value)}
          />
        </label>
        <button type="submit">Get Recommendations</button>
      </form>

      {recommendations.length > 0 && (
        <div>
          <h2>Recommendations for "{animeTitle}":</h2>
          <ul>
            {recommendations.map((anime, index) => (
              <li key={index}>{anime}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
