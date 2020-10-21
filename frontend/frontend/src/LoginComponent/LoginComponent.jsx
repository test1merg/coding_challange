import React, { useState } from 'react';
import axios from 'axios';


const LoginComponent = () => {

        const [email, setEmail] = useState("");
        const [password, setPassword] = useState("");
    

        const handleSubmit = (e) => {
            e.preventDefault();
            console.log(password);
            console.log(email);
            const data = {
                "email" : email,
                "password" : password
            };

            postCredentials(data);
        };

        const url = "http://127.0.0.1:8090"

        const postCredentials = async (data) => {
            const config = {
                method : 'post',
                url: url+ '/loginCreds',
                data : { data }
            }
            const response = await fetch(url)
            let req = await axios(config)
        }

        const getCredentials = async() => {
            const response = await fetch("")
        }




        return (
            <div className="Login">
                <form onSubmit= { handleSubmit }>
                    <label>Email
                    <input type="text" placeholder="Email" onChange= { e =>  setEmail(e.target.value) }/>
                    </label>

                    <label>Password
                        <input type="password" placeholder="Insert your Password" onChange= { e => setPassword(e.target.value)}></input>
                    </label>
                    <button type="submit">Submit</button>
                </form>
            </div>
        );
};


export default LoginComponent;