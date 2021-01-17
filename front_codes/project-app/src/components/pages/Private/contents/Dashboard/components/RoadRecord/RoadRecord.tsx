import React from 'react'
import { ArrowBack, ArrowForward, WatchLater, DirectionsRun, Opacity, InvertColors } from '@material-ui/icons';
import { IconButton, makeStyles, Typography } from '@material-ui/core';

const useStyles = makeStyles({
  top: {
    display: 'flex',
    justifyContent: 'space-between',
  },
  date: {
    marginTop: '12px',
  },
  content: {
    padding: '10px',
  },
  item : {
    display: 'flex',
    marginTop: '10px',
  }
})
 
const RoadRecord = () => {
  const classes = useStyles();
  return (
  <>
    <div className={classes.top}>
      <IconButton>
        <ArrowBack />
      </IconButton>
      <Typography className={classes.date}>2021.01.21</Typography>
      <IconButton>
        <ArrowForward />
      </IconButton>
    </div>
    <div className={classes.content}>
      <div className={classes.item}>
        <WatchLater />
        <Typography>총 주행시간: 3시간 12분</Typography>
      </div>
      <div className={classes.item}>
        <DirectionsRun />
        <Typography>총 주행거리: 192 Km</Typography>
      </div>
      <div className={classes.item}>
        <Opacity />
        <Typography>연비: 33.1 Km/L</Typography>
      </div>
      <div className={classes.item}>
        <InvertColors />
        <Typography>총 연료량: 5.8 L</Typography>
      </div>
    </div>
  </>
  )
}

export default RoadRecord;
