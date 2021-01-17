import React, { useEffect, useState } from 'react';
import clsx from 'clsx';
import { AppBar, Avatar, Badge, CssBaseline, Divider, Drawer, Icon, IconButton, List, ListItem, ListItemIcon, ListItemText, ListSubheader, ThemeProvider, Toolbar, Typography } from '@material-ui/core';
import { ChevronLeft, ExitToApp, Menu, Notifications, Settings,  } from '@material-ui/icons';
import ListItemData from './listItemData';

import useStyles from './styles';
import { useSelector, useDispatch } from 'react-redux';
import { RootState } from '../../../store';
import { setSuccess, signout } from '../../../store/actions/authActions';
import { NavLink, Route } from 'react-router-dom';
import Dashboard from './contents/Dashboard';
import Analysis from './contents/Analysis';
import { darkTheme, lightTheme } from '../../../theme/theme';
import SettingModal from './components/Setting/SettingModal';

export default function UserApp() {
  const classes = useStyles();
  const [open, setOpen] = React.useState(true);
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
  const [ theme, setTheme ] = useState(darkTheme)

  const openModal = () => {
    setOnModal(true);
  }

  const handleThemeChange = ( e: React.ChangeEvent<HTMLInputElement>, value: string ) => {
    if ( value === 'Dark' ) {
      setTheme(darkTheme);
    } else if ( value === 'Light') {
      setTheme(lightTheme);
    }
  }

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
            Dashboard
          </Typography>
          <IconButton color="inherit">
            <Badge badgeContent={4} color="secondary">
              <Notifications />
            </Badge>
          </IconButton>
          <IconButton color="inherit" onClick={openModal}>
            <Settings />
          </IconButton>
          <SettingModal onModal={onModal} setOnModal={setOnModal} />
          <IconButton color="inherit" onClick={logoutHandler}>
            <ExitToApp />
          </IconButton>
          <Avatar style={{ marginRight: 10 }}>{/* User Image */}</Avatar>
          <Typography>안녕하세요 {user?.firstName}님</Typography>
        </Toolbar>
      </AppBar>
      <Drawer
        variant="permanent"
        classes={{
          paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose),
        }}
        open={open}
      >
        <div className={classes.toolbarIcon}>
          <IconButton onClick={handleDrawerClose}>
            <ChevronLeft />
          </IconButton>
        </div>
        <Divider />
        <List>
          <ListSubheader
            className={clsx(!open && classes.hide)}
          >Reports
          </ListSubheader>
            { ListItemData.map((item, index) => (
              <NavLink 
                to={item.path} 
                style={{ textDecoration: 'none', color: 'rgba(0, 0, 0, 0.54)'}}
                activeClassName={ 'active' }
                activeStyle={{ color: '#3f51b5'}}
              >
                <ListItem button key={index}>
                  <ListItemIcon><Icon component={item.icon} /></ListItemIcon>
                  <ListItemText>{item.title}</ListItemText>
                </ListItem>
              </NavLink>
            ))}
        </List>
      </Drawer>
      <Route path="/app/dashboard" component={Dashboard} />
      <Route path="/app/analysis" component={Analysis} />
    </div>
  </ThemeProvider>
  );
}
