import React, { useEffect } from 'react';
import logging from "./config/logging";
import { BrowserRouter, Route, Switch, RouteComponentProps } from "react-router-dom";
import routes from "./config/route";


const Application: React.FunctionComponent<{}> = props => {
    useEffect(() => {
        logging.info('Loading application.');
    }, [])

    return (
        <div>
            <BrowserRouter>
                <Switch>
                    {routes.map((route, idx) => {
                        return (
                            <Route
                                key={idx}
                                path={route.path}
                                exact={route.exact}
                                render={(props: RouteComponentProps<any>) => (
                                    <route.component
                                        name={route.name}
                                        {...props}
                                        {...route.props}
                                    />
                                )}
                            />
                        );
                    })}
                </Switch>
            </BrowserRouter>
        </div>
    );
}

export default Application;