import React, { Component } from 'react'
import * as V from 'victory';
import { VictoryChart } from 'victory';
import { VictoryScatter } from 'victory';
import { VictoryZoomContainer } from 'victory';
import { VictoryLine } from 'victory';
import { VictoryBrushContainer } from 'victory';
import { VictoryAxis } from 'victory';
import { VictoryStack } from 'victory';
import { VictoryBar } from 'victory';
import { VictoryTheme } from 'victory';
import { VictoryPolarAxis } from 'victory';
import { Bar } from 'victory';



const data = [
  {quarter: 1, earnings: 13000},
  {quarter: 2, earnings: 16500},
  {quarter: 3, earnings: 14250},
  {quarter: 4, earnings: 19000}
];

class MoneyGraph extends React.Component {
  render() {
    return (
      <VictoryChart
        // adding the material theme provided with Victory
        theme={VictoryTheme.material}
        domainPadding={20}
      >
        <VictoryAxis
          tickValues={[1, 2, 3, 4]}
          tickFormat={["Axon 7", "1080ti", "ZeenBook 3", "ACER TV"]}
        />
        <VictoryAxis
          dependentAxis
          tickFormat={(x) => (`$${x / 1000}k`)}
        />
        <VictoryBar
          data={data}
          x="quarter"
          y="earnings"
        />
      </VictoryChart>
    )
  }
}


export default MoneyGraph

