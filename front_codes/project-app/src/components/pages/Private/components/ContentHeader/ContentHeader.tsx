import React, { FC } from 'react'
import { Breadcrumbs, Typography } from '@material-ui/core';

const ContentHeader: FC = () => {
  let pathname = window.location.pathname;
  const pathnames = pathname.split('/').filter((x) => x);
  const firstPathnameUpper = pathnames[1].charAt(0).toUpperCase();
  
  return (
    <Breadcrumbs separator=">" >
      <Typography>
        {firstPathnameUpper + pathnames[1].slice(1)}
      </Typography>
    </Breadcrumbs>
  )
}

export default ContentHeader;
