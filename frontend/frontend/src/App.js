import React, {useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import LoginComponent from './LoginComponent/LoginComponent';
import AuthWebSite from './AuthWebSite/AuthWebSite';

function App() {

  const [ login, setLogin ] = useState(false);

  const handleLogin = (changedLogin) => {
      setLogin(changedLogin);
  }



  return login ? (
      <AuthWebSite handleLogin = { handleLogin }></AuthWebSite>
    ) :
    (
      <div className="App">
        <h1> hello { login.toString() } </h1>
        <LoginComponent handleLogin = { handleLogin }/>
      </div>
  );
}

export default App;
