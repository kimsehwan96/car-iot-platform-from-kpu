import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import ListSubheader from '@material-ui/core/ListSubheader';
import DashboardIcon from '@material-ui/icons/Dashboard';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import PeopleIcon from '@material-ui/icons/People';
import BarChartIcon from '@material-ui/icons/BarChart';
import LayersIcon from '@material-ui/icons/Layers';
import AssignmentIcon from '@material-ui/icons/Assignment';

export const mainListItems = (
  <div>
    <ListItem button>
      <ListItemIcon>
        <DashboardIcon color="secondary"/>
      </ListItemIcon>
      <ListItemText primary="Dashboard" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <ShoppingCartIcon color="secondary"/>
      </ListItemIcon>
      <ListItemText primary="Item2" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <PeopleIcon color="secondary"/>
      </ListItemIcon>
      <ListItemText primary="Item3" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <BarChartIcon color="secondary"/>
      </ListItemIcon>
      <ListItemText primary="Item4" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <LayersIcon color="secondary"/>
      </ListItemIcon>
      <ListItemText primary="Item5" />
    </ListItem>
  </div>
);

export const secondaryListItems = (
  <div>
    <ListSubheader inset color="inherit">통계 자료</ListSubheader>
    <ListItem button>
      <ListItemIcon>
        <AssignmentIcon color="secondary"/>
      </ListItemIcon>
      <ListItemText primary="Day's Data" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <AssignmentIcon color="secondary"/>
      </ListItemIcon>
      <ListItemText primary="Month's Data" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <AssignmentIcon color="secondary"/>
      </ListItemIcon>
      <ListItemText primary="Year's Data" />
    </ListItem>
  </div>
);