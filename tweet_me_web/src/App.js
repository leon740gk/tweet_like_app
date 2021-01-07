import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from "react";

function loadTweets(callback) {
    const xhr = new XMLHttpRequest()
    const method = 'GET'
    const url = 'http://127.0.0.1:8000/api/tweets/'

    xhr.responseType = 'json'
    xhr.open(method, url)
    xhr.onload = function() {
        callback(xhr.response, xhr.status)
    }
    xhr.onerror = function(e) {
        console.log(e)
        callback("Error occurred", 400)
    }
    xhr.send()
}

function ActionBtn(props) {
    const {tweet, action} = props
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    return action.type === "like" ? <button className={className}>{tweet.likes} Like</button> : null
}

function Tweet(props) {
    const {tweet} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className}>
        <p>{tweet.id} - {tweet.content}</p>
        <div className="btn btn-group">
            <ActionBtn tweet={tweet} action={{type: "like"}}/>
            <ActionBtn tweet={tweet} action={{type: "unlike"}}/>
        </div>
    </div>
}

function App() {
  const [tweets, setTweets] = useState([])
  useEffect(() => {
    const tweetLoadCallback = (response, status) => {
      if (status === 200) {
        setTweets(response)
      } else {
        alert("Something went wrong...")
      }
    }
    loadTweets(tweetLoadCallback)
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
          {tweets.map((item, index)=>{
            return <Tweet tweet={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`}/>
          })}
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
