import * as React from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { useGoogleLogin } from '@react-oauth/google';
import { googleLogout } from '@react-oauth/google';
import { GoogleLogin } from '@react-oauth/google';
import {useState, useEffect} from "react";

import "../styles/Account.scss";

function Account() {
    const [access_token, set_token] = useState('');
    const login = useGoogleLogin({onSuccess: tokenResponse => set_token(tokenResponse.access_token)});
//     const login = useGoogleLogin({onSuccess: tokenResponse => console.log(tokenResponse)});

    // Тестовый запрос на backend (авторизация)
    useEffect(() => {
        const headers = {'Content-Type': 'application/json', 'Authorization': access_token}
        const data = { title: 'Тут потом будет запрос' };
        axios.post('http://localhost:8000/auth/user_init', data, { headers } )
            .then(function (response) {console.log(response);})
            .catch(function (error) {console.log(error);
        });
    }, [access_token]);




      return (
        <div>
            <div className='center_column'>
                <h2>Login</h2>
                <button className='button_mini' onClick={() => login()}>Sign in with Google 🚀</button>
                <button className='button_mini' onClick={() => googleLogout()}>Logout</button>
            </div>
{/*             {access_token} */}
{/*         <GoogleLogin onSuccess={credentialResponse => {console.log(credentialResponse);}} */}
{/*           onError={() => {console.log('Login Failed');}} */}
{/*           useOneTap */}
{/*         /> */}


        </div>
      );
    }


    function TestConnect() {
      return (
        <div>
          <h2>Dashboard</h2>
        </div>
      );
}



export default Account;
