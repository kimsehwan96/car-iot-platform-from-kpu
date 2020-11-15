import React, { useState, useEffect } from 'react'
import axios from 'axios';
import { Liquid } from '@ant-design/charts';

const api = axios.create({
  baseURL: 'https://43nssttj65.execute-api.ap-northeast-2.amazonaws.com/dev/oilstatus?userID=Hello%20world'
})

export default function Payload () {
  const [payload, setPayload] = useState({ id: '', percent: 0 });

  useEffect(() => {
    api.get('/').then(res => {
      console.log(res.data);
      setPayload(res.data);
    });
  }, []);

  const config = {
    appendPadding: 10,
    height: 300,
    percent: payload.percent,
    statistic: {
      content: {
        style: {
          fontSize: 60,
          fill: 'black',
        },
      },
    },
  };

  return <Liquid {...config} />;
}