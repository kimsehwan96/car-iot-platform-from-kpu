import React, { useEffect } from 'react';
import clsx from 'clsx';
import { AppBar, Avatar, Badge, CssBaseline, Divider, Drawer, Icon, IconButton, List, ListItem, ListItemIcon, ListItemText, ListSubheader, Toolbar, Typography } from '@material-ui/core';
import { ChevronLeft, ExitToApp, Menu, Notifications, Settings,  } from '@material-ui/icons';
import ListItemData from './listItemData';

import useStyles from './styles';
import { useSelector, useDispatch } from 'react-redux';
import { RootState } from '../../../store';
import { setSuccess, signout } from '../../../store/actions/authActions';
import { Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Analysis from './components/Analysis';

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
  
  return (
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
          <IconButton color="inherit">
            <Settings />
          </IconButton>
          <IconButton color="inherit" onClick={logoutHandler}>
            <ExitToApp />
          </IconButton>
          <Avatar>{/* User Image */}</Avatar>
          <Typography>{user?.firstName}</Typography>
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
              <ListItem button key={index}>
                <ListItemIcon><Icon component={item.icon} /></ListItemIcon>
                <ListItemText>{item.title}</ListItemText>
              </ListItem>
            ))}
        </List>
      </Drawer>
      <Route path="/app/dashboard" component={Dashboard} />
      <Route path="/app/analysis" component={Analysis} />
    </div>
  );
}
