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

const data = [
  { x: "Day 0", y: 24 },
  { x: "Day 1", y: 75 },
  { x: "Day 2", y: 98 },
  { x: "Day 3", y: 76 },
  { x: "Day 4", y: 109 },
  { x: "Day 5", y: 76 }
];

const cartesianInterpolations = [
  "basis",
  "bundle",
  "cardinal",
  "catmullRom",
  "linear",
  "monotoneX",
  "monotoneY",
  "natural",
  "step",
  "stepAfter",
  "stepBefore"
];

const polarInterpolations = [
  "basis",
  "cardinal",
  "catmullRom",
  "linear"
];

const InterpolationSelect = ({ currentValue, values, onChange }) => (
  <select onChange={onChange} value={currentValue} style={{ width: 75 }}>
    {values.map(
      (value) => <option value={value} key={value}>{value}</option>
    )}
  </select>
);

class TrendChart  extends React.Component {
  constructor() {
    super();
    this.state = {
      interpolation: "linear",
      polar: false
    };
  }
  render() {
    return (
      <div>
        <InterpolationSelect
          currentValue={this.state.interpolation}
          values={this.state.polar ? polarInterpolations : cartesianInterpolations }
          onChange={(event) => this.setState({ interpolation: event.target.value })}
        />
        <input
          type="checkbox"
          id="polar"
          value={this.state.polar}
          onChange={
            (event) => this.setState({
              polar: event.target.checked,
              interpolation: "linear"
            })
          }
          style={{ marginLeft: 25, marginRight: 5 }}
        />
        <label htmlFor="polar">polar</label>
        <VictoryChart polar={this.state.polar} height={390}>
          <VictoryLine
            interpolation={this.state.interpolation} data={data}
            style={{ data: { stroke: "#c43a31" } }}
          />
          <VictoryScatter data={data}
            size={5}
            style={{ data: { fill: "#c43a31" } }}
          />
        </VictoryChart>
      </div>
    );
  }
}
export default TrendChart
