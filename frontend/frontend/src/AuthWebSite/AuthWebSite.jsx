import React, { useState } from 'react'
import DataStreamComponent from './DataStreamComponent';
import HistoricDataComponent from './HistoricDataComponent'


const AuthWebSite = ({ handleLogin }) => {

    const [loggedIn, setLoggedIn] = useState(true);

    const handleLogout = (e) => {
        e.preventDefault();
        handleLogin(false)
    }

    return (
        <>
        <h1>Welcome, logged in user! </h1>
        <button class="logoutBtn" onClick = { handleLogout }>Logout</button>

        <DataStreamComponent></DataStreamComponent>
        <hr></hr>
        <HistoricDataComponent></HistoricDataComponent>
         </>
    )
}

export default AuthWebSite;