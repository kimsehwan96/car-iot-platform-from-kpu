import React, { useEffect } from 'react';
import IPage from "../interfaces/page";
import logging from "../config/logging";

const LoginPage: React.FunctionComponent<IPage> = props => {
    useEffect(() =>{
        logging.info(`Loading ${props.name}`);
    }, [props.name])

    return <div>This is LoginPage</div>;
}

export default LoginPage;