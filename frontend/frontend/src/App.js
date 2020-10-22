import React, {useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import LoginComponent from './LoginComponent/LoginComponent';

function App() {

  const [ login, setLogin ] = useState(false);

  const handleLogin = (changedLogin) => {
      setLogin(changedLogin);
  }


  return (
    <>
      <div className="App">
        <h1> hello { login.toString() } </h1>
        <LoginComponent handleLogin = { handleLogin }/>
      </div>
    </>
  )

  // return login ? (
  //   <AuthWebSite></AuthWebSite>
  // ) :
  // (
  //   <div className="App">
  
  //     <LoginComponent handleLogin = { handleLogin } login = { login }/>
  //   </div>
  // );
}

export default App;
