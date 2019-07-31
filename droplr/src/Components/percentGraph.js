import React, { Component } from 'react'
import * as V from 'victory';
import { VictoryChart } from 'victory';
import { VictoryScatter } from 'victory';
import { VictoryZoomContainer } from 'victory';
import { VictoryLine } from 'victory';
import { VictoryBrushContainer } from 'victory';
import { VictoryAxis } from 'victory';
import { VictoryStack } from 'victory';
import { VictoryLabel } from 'victory';
import { VictoryBar } from 'victory';
import { VictoryTheme } from 'victory';
import { VictoryPolarAxis } from 'victory';
import { Bar } from 'victory';
import './percentGraph.css'



const data = [
  {quarter: 1, earnings: 13},
  {quarter: 2, earnings: 93},
  {quarter: 3, earnings: 56},
  {quarter: 4, earnings: 71}
];

class PercentGraph extends React.Component {
  render() {
    return (
      <div>
      <div className="headerTitle">Analytics: </div>
      <span className="headerTitle">Item Revenue</span>
      <span className="white">___________________________________________________________________________________</span>

      <span className="headerTitle">Item Sales</span>
      <span className="white">_______________________________________</span>
      <div className="info">
        <div style={{height: '40%', width: '40%'}}>
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
        </div>
        <div style={{height: '40%', width: '40%'}}>
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
          tickFormat={(x) => (`${(x / 100) * 100}%`)}
        />
        <VictoryBar
          data={data}
          x="quarter"
          y="earnings"
        />
      </VictoryChart>
      </div>
      </div>
      </div>
    )
  }
}


export default PercentGraph
