import React, { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'



const button = (
    <button>Subscribe</button>
)

const inputs = (
    <>
        <div className='input-wrapper'>
            <input type="firstName" placeholder='First Name'/>
            <input type="lastName" placeholder='Last Name'/>
            <input type="email" placeholder="E-Mail"/>
        </div>
    </>
)

function App() {
    return (
        <>
            <div className='subscribe-wrapper'>
                <h1>SUBSCRIBE</h1>
                <p>Sign up with your email address to receive news and updates</p>
                {inputs}
                {button}
            </div>
        </>
    )
}

export default App;
