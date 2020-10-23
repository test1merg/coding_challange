import React, { useState } from 'react';
import axios from 'axios';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
                                                                                   

const LoginComponent = ({ handleLogin }) => {

        const [email, setEmail] = useState("");
        const [password, setPassword] = useState("");
 
        const handleSubmit = (e) => {
            e.preventDefault();
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
            let response = await axios(config);
            handleLogin(response.data)
            
            
            return response.data;
        }

        // return (
        //     <div className="Login">
        //         <form onSubmit= { handleSubmit }>
        //             <label>Email
        //             <input type="text" placeholder="Email" onChange= { e =>  setEmail(e.target.value) }/>
        //             </label>

        //             <label>Password
        //                 <input type="password" placeholder="Insert your Password" onChange= { e => setPassword(e.target.value)}></input>
        //             </label>
        //             <button type="submit">Submit</button>
        //         </form>
        //     </div>
        // );

        const useStyles = makeStyles((theme) => ({
            paper: {
              marginTop: theme.spacing(8),
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            },
            avatar: {
              margin: theme.spacing(1),
              backgroundColor: theme.palette.secondary.main,
            },
            form: {
              width: '100%', // Fix IE 11 issue.
              marginTop: theme.spacing(1),
            },
            submit: {
              margin: theme.spacing(3, 0, 2),
            },
          }));

          const classes = useStyles();

          return (
            <Container component="main" maxWidth="xs">
              <CssBaseline />
              <div className={classes.paper}>
                <Avatar className={classes.avatar}>
                </Avatar>
                <Typography component="h1" variant="h5">
                  Sign in
                </Typography>
                <form className={classes.form} noValidate onSubmit= { handleSubmit }>
                  <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="email"
                    label="Email Address"
                    name="email"
                    autoComplete="email"
                    autoFocus
                    onChange= { e =>  setEmail(e.target.value) }
                  />
                  <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    name="password"
                    label="Password"
                    type="password"
                    id="password"
                    autoComplete="current-password"
                    onChange= { e => setPassword(e.target.value)}
                  />
                  <FormControlLabel
                    control={<Checkbox value="remember" color="primary" />}
                    label="Remember me"
                  />
                  <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
                    className={classes.submit}
                  >
                    Sign In
                  </Button>
                </form>
              </div>
              <Box mt={8}>
              </Box>
            </Container>
          );

};


export default LoginComponent;