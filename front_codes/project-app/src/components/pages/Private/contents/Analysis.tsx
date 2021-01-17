import React, { FC } from 'react'
import { Container, Grid, Paper } from '@material-ui/core';
import clsx from 'clsx';
import useStyles from '../styles';
import ContentHeader from '../components/ContentHeader/ContentHeader';

const Analysis: FC = () => {
  const classes = useStyles();
  const fixedHeightPaper = clsx(classes.paper, classes.fixedHeight);

  return (
    <main className={classes.content}>
      <div className={classes.appBarSpacer} />
      <Container maxWidth="lg" className={classes.container}>
        <ContentHeader />
        <Grid container spacing={3}>
          {/* Chart */}
          <Grid item xs={12} md={8} lg={9}>
            <Paper className={fixedHeightPaper}>
              {/* <Chart /> */}
            </Paper>
          </Grid>
          {/* Recent Deposits */}
          <Grid item xs={12} md={4} lg={3}>
            <Paper className={fixedHeightPaper}>
              {/* <Deposits /> */}
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

export default Analysis;
