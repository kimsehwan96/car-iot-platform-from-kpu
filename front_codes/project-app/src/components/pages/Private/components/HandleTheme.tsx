import { createStyles, FormGroup, Grid, Switch, Theme, Typography, withStyles } from '@material-ui/core';
import React, { FC, useState } from 'react'

const AntSwitch = withStyles((theme: Theme) =>
  createStyles({
    root: {
      width: 28,
      height: 16,
      padding: 0,
      display: 'flex',
    },
    switchBase: {
      padding: 2,
      color: theme.palette.grey[500],
      '&$checked': {
        transform: 'translateX(12px)',
        color: '#3f51b5',
        '& + $track': {
          opacity: 1,
          backgroundColor: '#fff',
          borderColor: theme.palette.primary.main,
        },
      },
    },
    thumb: {
      width: 12,
      height: 12,
      boxShadow: 'none',
    },
    track: {
      border: `1px solid ${theme.palette.grey[500]}`,
      borderRadius: 16 / 2,
      opacity: 1,
      backgroundColor: theme.palette.common.white,
    },
    checked: {},
  }),
)(Switch);

const HandleTheme: FC = () => {
  const [dark, setDark] = useState(true);

  const handleChange = () => {
    setDark((prev: boolean) => !prev);
  }

  return (
    <FormGroup>
      <Typography>
        <Grid component="label" container alignItems="center" spacing={1}>
          <Grid item>Dark</Grid>
            <Grid item>
              <AntSwitch checked={dark} onChange={handleChange} name="checkedC" />
            </Grid>
          <Grid item>Light</Grid>
        </Grid>
      </Typography>
    </FormGroup>
  )
}

export default HandleTheme;