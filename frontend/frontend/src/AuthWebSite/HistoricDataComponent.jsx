

import React, { useState } from 'react';
import axios from 'axios';
import BorderWrapper from 'react-border-wrapper'


const HistoricDataComponent = () => {

    const [name, setName] = useState("");
    const [limit, setLimit ] = useState(25);
    const [results, setResult ] = useState("");

    
    const handleSubmit = (e) => {
    
        e.preventDefault();
        // const data = {
        //     "counterparty_name" : name,
        //     "limit" : limit
        // };
        postParamtersForHistoricData(name, limit);
    }
    const url = "http://127.0.0.1:8090/historicData"
    const postParamtersForHistoricData = async (name, limit) => {
        console.log(`url of historic is ${url}/${name}/${limit}`);
        let response = await axios.get(`${url}/${name}/${limit}`);
        setResult(response.data);
    }

    return (
        <>
            <BorderWrapper>
                <div>
                    <form onSubmit = { handleSubmit }>
                        <label>Counterparty Name
                        <input type="text" placeholder="CounterpartName" onChange={e => setName(e.target.value)}/>
                        </label>
                        <label>Limit
                        <input type="text" placeholder="Limit" onChange={e => setLimit(e.target.value)}/>
                        </label>
                        <button type="submit">Get Historic Data!</button>
                    </form>
                
                </div>
                <div>
                    {results}
                </div>
            </BorderWrapper>
        </>
    )
}
export default HistoricDataComponent;
