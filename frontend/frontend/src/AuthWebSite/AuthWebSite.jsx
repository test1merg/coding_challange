import React from 'react'
import DataStreamComponent from './DataStreamComponent';
import HistoricDataComponent from './HistoricDataComponent'


const AuthWebSite = () => {

    return (
        <>
        <h1>Welcome, logged in user! </h1>
        <DataStreamComponent></DataStreamComponent>
        <hr></hr>
        <HistoricDataComponent></HistoricDataComponent>
         </>
    )
}

export default AuthWebSite;