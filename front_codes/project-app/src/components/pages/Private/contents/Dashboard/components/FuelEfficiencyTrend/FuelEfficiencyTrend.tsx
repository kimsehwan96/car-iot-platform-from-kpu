import React from 'react'
import { AppBar, Box, makeStyles, Tab, Tabs, Theme, Typography, useTheme } from '@material-ui/core';
import SwipeableViews from 'react-swipeable-views'
import DayChart from './Charts/DayChart';
import WeekChart from './Charts/WeekChart';
import MonthChart from './Charts/MonthChart';
 
interface TabPanelProps {
  children?: React.ReactNode;
  dir?: string;
  index: any;
  value: any;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`full-width-tabpanel-${index}`}
      aria-labelledby={`full-width-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box p={3}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

function a11yProps(index: any) {
  return {
    id: `full-width-tab-${index}`,
    'aria-controls': `full-width-tabpanel-${index}`,
  };
}

const useStyles = makeStyles((theme: Theme) => ({
  root: {
    backgroundColor: theme.palette.background.paper,
    width: '100%',
    height: '100%',
    padding: 0,
  },
}));

export const FuelEfficiencyTrend = () => {
  const classes = useStyles();
  const theme = useTheme();
  const [value, setValue] = React.useState(0);

  const handleChange = (event: React.ChangeEvent<{}>, newValue: number) => {
    setValue(newValue);
  };

  const handleChangeIndex = (index: number) => {
    setValue(index);
  };

  return (
    <div className={classes.root}>
      <AppBar position="relative">
        <Tabs
          value={value}
          onChange={handleChange}
          indicatorColor="primary"
          textColor="primary"
          variant="scrollable"
        >
          <Tab label="Day" {...a11yProps(0)} />
          <Tab label="Week" {...a11yProps(1)} />
          <Tab label="Month" {...a11yProps(2)} />
        </Tabs>
      </AppBar>
      <SwipeableViews
        axis={theme.direction === 'rtl' ? 'x-reverse' : 'x'}
        index={value}
        onChangeIndex={handleChangeIndex}
      >
        <TabPanel value={value} index={0} dir={theme.direction}>
          <DayChart/>
        </TabPanel>
        <TabPanel value={value} index={1} dir={theme.direction}>
          <WeekChart />
        </TabPanel>
        <TabPanel value={value} index={2} dir={theme.direction}>
          <MonthChart />
        </TabPanel>
      </SwipeableViews>
    </div>
  );
}

export default FuelEfficiencyTrend;