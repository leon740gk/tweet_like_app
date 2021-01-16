import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {TweetsComponent} from "./tweets"


const rootEl = document.getElementById('root')
const tweetRootEl = document.getElementById('tweet-root')
if (rootEl) {
    ReactDOM.render(
      <React.StrictMode>
        <App />
      </React.StrictMode>,
      rootEl
    );
}
if (tweetRootEl) {
    ReactDOM.render(
      <React.StrictMode>
        <TweetsComponent />
      </React.StrictMode>,
      tweetRootEl
    );
}



// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
