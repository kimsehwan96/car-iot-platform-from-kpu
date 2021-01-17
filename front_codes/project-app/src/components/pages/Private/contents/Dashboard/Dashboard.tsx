import { Container, Grid, Paper } from '@material-ui/core';
import clsx from 'clsx';
import React, { FC } from 'react';
import useStyles from '../../styles';
import ContentHeader from '../../components/ContentHeader/ContentHeader';
import RoadRecord from './components/RoadRecord/RoadRecord';

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
            <Paper className={fixedHeightPaper}>
              {/* <Data /> */}
            </Paper>
          </Grid>
          <Grid item xs={12} md={6} lg={4}>
            <Paper className={fixedHeightPaper}>
              {/* <Data /> */}
            </Paper>
          </Grid>
          {/* Recent Orders */}
          <Grid item xs={12}>
            <Paper className={classes.paper}>
              {/* <Orders /> */}
            </Paper>
          </Grid>
        </Grid>
      </Container>
    </main>
  )
}

export default Dashboard;
