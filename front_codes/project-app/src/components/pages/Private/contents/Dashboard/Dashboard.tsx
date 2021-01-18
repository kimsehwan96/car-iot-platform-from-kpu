import { Container, Grid, Paper } from '@material-ui/core';
import clsx from 'clsx';
import React, { FC } from 'react';
import useStyles from '../../styles';
import ContentHeader from '../../components/ContentHeader/ContentHeader';
import RoadRecord from './components/RoadRecord/RoadRecord';
import FuelEfficiencyTrend from './components/FuelEfficiencyTrend/FuelEfficiencyTrend';
import KakaoMap from './components/KaKaoMap/KakaoMap';

const Dashboard: FC = () => {
  const classes = useStyles();
  const fixedHeightPaper = clsx(classes.paper, classes.fixedHeight);

  return (
    <main className={classes.content}>
      <div className={classes.appBarSpacer} />
      <Container maxWidth="lg" className={classes.container}>
        <ContentHeader />
        <Grid container spacing={3}>
          <Grid item xs={12} md={6} lg={4}>
            <Paper className={fixedHeightPaper}>
              <RoadRecord />
            </Paper>
          </Grid>
          <Grid item xs={12} md={6} lg={4}>
            <div className={fixedHeightPaper} style={{ padding: 0, borderRadius: 5, zIndex: 1300, boxShadow:'0px 2px 1px -1px rgba(0,0,0,0.2), 0px 1px 1px 0px rgba(0,0,0,0.14), 0px 1px 3px 0px rgba(0,0,0,0.12)' }}>
              <FuelEfficiencyTrend />
            </div>
          </Grid>
          <Grid item xs={12} md={6} lg={4}>
            <Paper className={fixedHeightPaper}>
              {/* <Data /> */}
            </Paper>
          </Grid>
          {/* Recent Orders */}
          <Grid item xs={8}>
            <Paper className={classes.paper}>
              <KakaoMap />
            </Paper>
          </Grid>
          <Grid item xs={4}>
            <Paper className={classes.paper}>
              오늘의 주행기록
            </Paper>
          </Grid>
        </Grid>
      </Container>
    </main>
  )
}

export default Dashboard;
