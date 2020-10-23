import Axios from 'axios';
import React, { useState } from 'react'
import axios from 'axios';
import { useObservable } from 'rxjs-hooks';
import { Observable } from 'rxjs';
import { map, withLatestFrom } from 'rxjs/operators';
import BorderWrapper from 'react-border-wrapper'

const stringObservable = Observable.create(observer => {
    const url = 'http://localhost:8090/deals'

      const source = new EventSource(url);
        source.addEventListener('message', (messageEvent) => {
                console.log(messageEvent);
                    observer.next(messageEvent.data);
        }, false);
        });

const DataStreamComponent = () => {
    const [stringArray, setStringArray ] = useState([]);

    useObservable(
        state => 
            stringObservable.pipe(
                withLatestFrom(state),
                map(([state]) => {
                    let updatedStringArray = stringArray;
                    updatedStringArray.unshift(state);
                    if (updatedStringArray.length >= 5) {
                        updatedStringArray.pop();
                    }
                    setStringArray(updatedStringArray);
                    return state;
                })
            )
    );

    return (

    <>
    <BorderWrapper>
    {stringArray ? stringArray.map((message, index) => <p key={index}>{message}</p>) : <p>Loading...</p>}
    </BorderWrapper>
    </>
    )

}



export default DataStreamComponent;






// const DataStreamComponent = () => {

//     const url = 'http://localhost:8090/deals'

//    // const source = new EventSource(url);

//     if (!!window.EventSource) {
//         var source = new EventSource(url);
//         } else {
//                 // Result to xhr polling :(
//                 }

//     source.addEventListener('message', function(e) {
//           console.log(e.data);
//     }, false);


//     source.addEventListener('open', function(e) {
//           // Connection was opened.
//           }, false);
           
//     source.addEventListener('error', function(e) {
//         if (e.readyState == EventSource.CLOSED) {
//                          // Connection was CLOSED  
//                         }
//                          }, false);

// }

