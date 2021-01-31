import { Divider, Drawer, Icon, IconButton, List, ListItem, ListItemIcon, ListSubheader, Typography } from '@material-ui/core'
import { ChatBubble, ChevronLeft } from '@material-ui/icons'
import clsx from 'clsx'
import React, { FC } from 'react'
import { NavLink } from 'react-router-dom'
import ListItemData from '../../listItemData'

import useStyles from '../../styles';

interface NavebarProps {
  open: boolean;
  handleDrawerClose: any;
}
 
const Navbar: FC<NavebarProps> = ({ open, handleDrawerClose }) => {
  const classes = useStyles();

  return (
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
                style={{ textDecoration: 'none', color: "#adacac"}}
                activeClassName={ 'active' }
                activeStyle={{ color: '#3f51b5'}}
              >
                <ListItem button key={index}>
                  <ListItemIcon>
                    <Icon component={item.icon} />
                  </ListItemIcon>
                    <Typography>
                      {item.title}
                    </Typography>
                </ListItem>
              </NavLink>
            ))}
            <ListSubheader
              className={clsx(!open && classes.hide)}
            >
              Community
            </ListSubheader>
            <NavLink 
                to="chat" 
                style={{ textDecoration: 'none', color: "#adacac"}}
                activeClassName={ 'active' }
                activeStyle={{ color: '#3f51b5'}}
              >
                <ListItem button>
                  <ListItemIcon>
                    <ChatBubble />
                  </ListItemIcon>
                    <Typography>
                      Chat
                    </Typography>
                </ListItem>
              </NavLink>
        </List>
      </Drawer>
  )
}

export default Navbar;
