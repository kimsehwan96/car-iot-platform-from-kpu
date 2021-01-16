import React, { FC } from 'react';
import  Icon1  from '../../../asserts/4.svg';
import  Icon2  from '../../../asserts/5.svg';
import  Icon3  from '../../../asserts/6.svg';
import { ExpectationsCard, ExpectationsContainer, ExpectationsH1, ExpectationsH2, ExpectationsIcon, ExpectationsP, ExpectationsWrapper } from './expectationsElements';

const Expectations: FC = () => {
  return (
    <ExpectationsContainer id="expectations">
      <ExpectationsH1>Expectations</ExpectationsH1>
      <ExpectationsWrapper>
        <ExpectationsCard>
          <ExpectationsIcon src={Icon1} />
          <ExpectationsH2>Eco-friendly</ExpectationsH2>
          <ExpectationsP>
            Fuel economy can save fuel and reduce environmental pollution
          </ExpectationsP>
        </ExpectationsCard>
        <ExpectationsCard>
          <ExpectationsIcon src={Icon2}/>
          <ExpectationsH2>Accident prevention</ExpectationsH2>
          <ExpectationsP>
            Prevent accidents by identifying the hazardous conditions of the vehicle in advance
          </ExpectationsP>
        </ExpectationsCard>
        <ExpectationsCard>
          <ExpectationsIcon src={Icon3}/>
          <ExpectationsH2>Economic Effect</ExpectationsH2>
          <ExpectationsP>
            Economic effects can be achieved by reducing fuel costs through fuel economy operation
          </ExpectationsP>
        </ExpectationsCard>
      </ExpectationsWrapper>
    </ExpectationsContainer>
  )
}

export default Expectations;
