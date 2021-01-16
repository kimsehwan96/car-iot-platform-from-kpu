import React, { FC } from 'react';
import { useSelector } from 'react-redux';
import { Redirect, Route, RouteProps } from 'react-router-dom';

import { RootState } from '../../store';

interface Props extends RouteProps {
  component: any;
}

const PrivateRoute: FC<Props> = ({ component: Component, ...rest }) => {
  const { authenticated } = useSelector((state: RootState) => state.auth);

  return (
    <section>
      <Route {...rest} render={props => authenticated ? <Component {...props} /> : <Redirect to='/signin' />}></Route>
    </section>
  )
}

export default PrivateRoute;
