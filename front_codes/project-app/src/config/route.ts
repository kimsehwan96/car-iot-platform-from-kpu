import IRoute from "../interfaces/routes";
import HomePage from "../pages/home";
import LoginPage from "../pages/login";

const routes: IRoute[] = [
    {
        path: '/',
        name: 'Home Page',
        component: HomePage,
        exact: true,
    },
    {
        path: '/login',
        name: 'Login Page',
        component: LoginPage,
        exact: true,
    }
]

export default routes;