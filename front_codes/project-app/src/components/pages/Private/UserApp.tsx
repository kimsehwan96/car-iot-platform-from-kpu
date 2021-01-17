import React, { useEffect, useState } from 'react';
import clsx from 'clsx';
import { AppBar, Avatar, Badge, createMuiTheme, CssBaseline, IconButton, ThemeProvider, Toolbar, Typography } from '@material-ui/core';
import { ExitToApp, Menu, Notifications, Settings,  } from '@material-ui/icons';

import useStyles from './styles';
import { useSelector, useDispatch } from 'react-redux';
import { RootState } from '../../../store';
import { setSuccess, signout } from '../../../store/actions/authActions';
import { Route } from 'react-router-dom';
import Dashboard from './contents/Dashboard/Dashboard';
import Analysis from './contents/Analysis';
import SettingModal from './components/Setting/SettingModal';
import userImg from './img/userImg.jpg'
import Navbar from './components/Navbar/Navbar';

export default function UserApp() {
  const classes = useStyles();
  const [open, setOpen] = useState(true);
  const dispatch = useDispatch();
  const { success, user } = useSelector((state: RootState) => state.auth);

  useEffect(() => {
    if (success) {
      dispatch(setSuccess(''));
    }
  }, [success, dispatch]);

  const logoutHandler = () => {
    dispatch(signout());
  }

  const handleDrawerOpen = () => {
    setOpen(true);
  };
  const handleDrawerClose = () => {
    setOpen(false);
  };
  
  // Theme Handler
  const [onModal, setOnModal] = useState(false);
  const [darkMode , setDarkMode] = useState(true);

  const openModal = () => {
    setOnModal(true);
  }

  const theme = createMuiTheme({
    palette : {
      type: darkMode ? 'dark' : 'light',
      primary: {
        main: darkMode? '#3F51B5' : '#3f50b5',
      },
    },
    overrides: {
      MuiAppBar: {
        colorPrimary: {
          backgroundColor :'#202020',
        }
      },
      MuiTab: {
        root: {
          minWidth: '110px',
        }
      }
    }
  });

  return (
  <ThemeProvider theme={theme}>
    <div className={classes.root}>
      <CssBaseline />
      <AppBar position="absolute" className={clsx(classes.appBar, open && classes.appBarShift)}>
        <Toolbar className={classes.toolbar}>
          <IconButton
            edge="start"
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            className={clsx(classes.menuButton, open && classes.menuButtonHidden)}
          >
            <Menu />
          </IconButton>
          <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
            UserApp
          </Typography>
          <IconButton color="inherit">
            <Badge badgeContent={4} color="secondary">
              <Notifications />
            </Badge>
          </IconButton>
          <IconButton color="inherit" onClick={openModal}>
            <Settings />
          </IconButton>
          <SettingModal 
            onModal={onModal} 
            setOnModal={setOnModal} 
            darkMode={darkMode} 
            setDarkMode={setDarkMode} 
          />
          <IconButton color="inherit" onClick={logoutHandler}>
            <ExitToApp />
          </IconButton>
          <Typography>안녕하세요 {user?.firstName}님</Typography>
          <Avatar style={{ marginLeft: 10 }} src={userImg} />
        </Toolbar>
      </AppBar>
      <Navbar open={open} handleDrawerClose={handleDrawerClose} />
      <Route path="/app/dashboard" component={Dashboard} />
      <Route path="/app/analysis" component={Analysis} />
    </div>
  </ThemeProvider>
  );
}
