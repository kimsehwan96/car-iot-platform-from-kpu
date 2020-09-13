import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardActionArea, CardContent, Typography } from '@material-ui/core';
import ReactSpeedometer from 'react-d3-speedometer';

const useStyles = makeStyles ({
    rpmMeter: {
        color: "#fff",
        marginTop: 20,
        maxWidth: 345,
        backgroundColor: '#323232',
        display: 'inline-flex'
    },
    speedoMeter: {
        color: "#fff",
        marginTop: 20,
        maxWidth: 345,
        backgroundColor: '#323232',
        display: 'inline-flex',
        marginLeft: '20px',
    },
});

let getRandomInt = (min, max) => {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
}

export default function Speedometer() {
    const classes = useStyles();

    return (
    <div className={classes.root}>
        <Card className={classes.rpmMeter}>
            <CardActionArea>
                <ReactSpeedometer
                maxValue= "1000"
                startColor="green"
                endColor="red"
                needleColor= "white"
                value= {getRandomInt(700,1000)}
                />
                <CardContent> 
                    <Typography gutterBottom variant="h5" component="h2">
                        RPM
                    </Typography>
                    <Typography variant="body2" color="white" component="h2">
                        1분당 회전수(엔진)
                    </Typography>
                </CardContent>
            </CardActionArea>
        </Card>
        <Card className={classes.speedoMeter}>
        <CardActionArea>
            <ReactSpeedometer
            maxValue= "250"
            startColor="green"
            endColor="red"
            needleColor= "white"
            value= {getRandomInt(0,250)}
            />
            <CardContent> 
                <Typography gutterBottom variant="h5" component="h2">
                    SPEED
                </Typography>
                <Typography variant="body2" color="white" component="h2">
                    시간당 이동한 거리
                </Typography>
            </CardContent>
        </CardActionArea>
    </Card>
    </div>
    )
}