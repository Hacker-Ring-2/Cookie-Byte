'use client';

import React, { useState } from 'react';
import dynamic from 'next/dynamic';
import { COLOR_PALETTE, getResponsiveConfig } from '@/utils/plotly';
import { useScreen } from '@/hooks/use-screen';
import useWindowDimension from '@/hooks/useWindowDimension';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';

// Dynamically import Plotly to avoid SSR issues
const Plot = dynamic(
  () =>
    import('react-plotly.js/factory').then((mod) => {
      const Plotly = require('plotly.js-basic-dist');
      return mod.default(Plotly);
    }),
  { ssr: false }
);

const FinancialChartExamples = () => {
  const { screen: screenSize, containerWidth } = useScreen();
  const { windowDimension } = useWindowDimension();
  const { height: windowHeight } = windowDimension;
  const config = getResponsiveConfig(screenSize, windowHeight, 400, true);
  
  // Sample data for financial charts
  const pieChartData = {
    labels: ['Stocks', 'Bonds', 'Real Estate', 'Cash', 'Commodities'],
    values: [45, 25, 15, 10, 5],
    title: 'Portfolio Asset Allocation'
  };
  
  const barChartData = {
    x: ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024'],
    y: [120, 150, 170, 190, 210],
    title: 'Quarterly Revenue (in millions $)'
  };
  
  const lineChartData = {
    x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    y: [50, 60, 40, 70, 80, 90, 100, 110, 90, 120, 130, 150],
    title: 'Monthly Stock Price Performance'
  };
  
  const multiLineChartData = {
    x: ['2019', '2020', '2021', '2022', '2023'],
    series: [
      { name: 'Revenue', y: [200, 250, 300, 350, 400] },
      { name: 'Profit', y: [50, 70, 90, 110, 130] },
      { name: 'Expenses', y: [150, 180, 210, 240, 270] }
    ],
    title: 'Financial Performance (in millions $)'
  };

  // Generate pie chart
  const renderPieChart = () => {
    const data = [{
      type: 'pie',
      labels: pieChartData.labels,
      values: pieChartData.values,
      textinfo: screenSize === 'mobile' ? 'percent' : 'label+percent',
      textposition: screenSize === 'mobile' ? 'inside' : 'outside',
      marker: {
        colors: pieChartData.labels.map(
          (_: any, index: number) => COLOR_PALETTE[index % COLOR_PALETTE.length]
        ),
        line: {
          color: '#FFFFFF',
          width: screenSize === 'mobile' ? 1 : 2,
        },
      },
      insidetextorientation: 'radial',
    }];

    const layout = {
      title: {
        text: pieChartData.title,
        font: {
          size: config.titleFontSize,
          family: 'Inter, sans-serif',
          color: '#1F2937',
        },
        x: 0.5,
        xanchor: 'center',
      },
      margin: config.margins,
      showlegend: true,
      legend: {
        orientation: 'h',
        y: screenSize === 'mobile' ? -0.1 : -0.2,
        x: 0.5,
        xanchor: 'center',
        yanchor: 'top',
        bgcolor: 'transparent',
        bordercolor: '#E5E7EB',
        borderwidth: 0,
        font: { size: screenSize === 'mobile' ? 10 : 12 },
      },
      paper_bgcolor: '#f1f1e2',
      plot_bgcolor: '#f1f1e2',
      font: {
        family: 'Inter, sans-serif',
        color: '#374151',
        size: config.tickFontSize,
      },
    };

    return { data, layout };
  };

  // Generate bar chart
  const renderBarChart = () => {
    const data = [{
      type: 'bar',
      x: barChartData.x,
      y: barChartData.y,
      marker: {
        color: COLOR_PALETTE[0],
        opacity: 0.8,
        line: {
          color: COLOR_PALETTE[0],
          width: screenSize === 'mobile' ? 1 : 2,
        },
      },
    }];

    const layout = {
      title: {
        text: barChartData.title,
        font: {
          size: config.titleFontSize,
          family: 'Inter, sans-serif',
          color: '#1F2937',
        },
        x: 0.5,
        xanchor: 'center',
      },
      margin: config.margins,
      showlegend: false,
      paper_bgcolor: '#f1f1e2',
      plot_bgcolor: '#f1f1e2',
      font: {
        family: 'Inter, sans-serif',
        color: '#374151',
        size: config.tickFontSize,
      },
      xaxis: {
        title: 'Quarter',
        titlefont: {
          size: config.axisLabelFontSize,
        },
      },
      yaxis: {
        title: 'Revenue (millions $)',
        titlefont: {
          size: config.axisLabelFontSize,
        },
      },
    };

    return { data, layout };
  };

  // Generate line chart
  const renderLineChart = () => {
    const data = [{
      type: 'scatter',
      mode: 'lines+markers',
      x: lineChartData.x,
      y: lineChartData.y,
      line: {
        width: screenSize === 'mobile' ? 2 : 3,
        color: COLOR_PALETTE[2],
      },
      marker: {
        size: screenSize === 'mobile' ? 4 : 6,
        color: COLOR_PALETTE[2],
        line: {
          color: '#FFFFFF',
          width: screenSize === 'mobile' ? 1 : 2,
        },
      },
    }];

    const layout = {
      title: {
        text: lineChartData.title,
        font: {
          size: config.titleFontSize,
          family: 'Inter, sans-serif',
          color: '#1F2937',
        },
        x: 0.5,
        xanchor: 'center',
      },
      margin: config.margins,
      showlegend: false,
      paper_bgcolor: '#f1f1e2',
      plot_bgcolor: '#f1f1e2',
      font: {
        family: 'Inter, sans-serif',
        color: '#374151',
        size: config.tickFontSize,
      },
      xaxis: {
        title: 'Month',
        titlefont: {
          size: config.axisLabelFontSize,
        },
      },
      yaxis: {
        title: 'Stock Price ($)',
        titlefont: {
          size: config.axisLabelFontSize,
        },
      },
    };

    return { data, layout };
  };

  // Generate multi-line chart
  const renderMultiLineChart = () => {
    const data = multiLineChartData.series.map((series, index) => ({
      type: 'scatter',
      mode: 'lines+markers',
      name: series.name,
      x: multiLineChartData.x,
      y: series.y,
      line: {
        width: screenSize === 'mobile' ? 2 : 3,
        color: COLOR_PALETTE[index % COLOR_PALETTE.length],
      },
      marker: {
        size: screenSize === 'mobile' ? 4 : 6,
        color: COLOR_PALETTE[index % COLOR_PALETTE.length],
        line: {
          color: '#FFFFFF',
          width: screenSize === 'mobile' ? 1 : 2,
        },
      },
    }));

    const layout = {
      title: {
        text: multiLineChartData.title,
        font: {
          size: config.titleFontSize,
          family: 'Inter, sans-serif',
          color: '#1F2937',
        },
        x: 0.5,
        xanchor: 'center',
      },
      margin: config.margins,
      showlegend: true,
      legend: {
        orientation: 'h',
        y: screenSize === 'mobile' ? -0.1 : -0.2,
        x: 0.5,
        xanchor: 'center',
        yanchor: 'top',
        bgcolor: 'transparent',
        bordercolor: '#E5E7EB',
        borderwidth: 0,
        font: { size: screenSize === 'mobile' ? 10 : 12 },
      },
      paper_bgcolor: '#f1f1e2',
      plot_bgcolor: '#f1f1e2',
      font: {
        family: 'Inter, sans-serif',
        color: '#374151',
        size: config.tickFontSize,
      },
      xaxis: {
        title: 'Year',
        titlefont: {
          size: config.axisLabelFontSize,
        },
      },
      yaxis: {
        title: 'Amount (millions $)',
        titlefont: {
          size: config.axisLabelFontSize,
        },
      },
    };

    return { data, layout };
  };

  const pieChart = renderPieChart();
  const barChart = renderBarChart();
  const lineChart = renderLineChart();
  const multiLineChart = renderMultiLineChart();

  const plotConfig = {
    responsive: true,
    displayModeBar: screenSize !== 'mobile',
    modeBarButtonsToRemove: [
      'lasso2d',
      'zoom2d',
      'select2d',
      'autoScale2d',
      'hoverClosestCartesian',
      'hoverCompareCartesian',
      'toggleSpikelines',
    ] as any,
    displaylogo: false,
    toImageButtonOptions: {
      format: 'png' as const,
      filename: 'financial_chart',
      height: config.dynamicHeight,
      width: Math.max(containerWidth * 0.9, 600),
      scale: 1.5,
    },
    dragmode: 'pan',
  };

  return (
    <div className="w-full p-4">
      <h1 className="text-2xl font-bold mb-6 text-center">Financial Chart Examples</h1>
      <p className="text-center mb-6 text-gray-600">Demonstrating the enhanced chart capabilities using react-plotly.js</p>
      
      <Tabs defaultValue="pie" className="w-full">
        <TabsList className="grid w-full grid-cols-4">
          <TabsTrigger value="pie">Pie Chart</TabsTrigger>
          <TabsTrigger value="bar">Bar Chart</TabsTrigger>
          <TabsTrigger value="line">Line Chart</TabsTrigger>
          <TabsTrigger value="multiline">Multi-Line Chart</TabsTrigger>
        </TabsList>
        
        <TabsContent value="pie" className="mt-4">
          <div className="w-full bg-white rounded-lg shadow-sm border border-gray-200">
            <div className="w-full p-2 sm:p-4 bg-[var(--primary-chart-bg)]">
              <Plot
                data={pieChart.data}
                layout={pieChart.layout}
                config={plotConfig}
                style={{
                  width: '100%',
                  height: `${config.dynamicHeight}px`,
                  minHeight: '300px',
                }}
                useResizeHandler={true}
                className="w-full"
              />
            </div>
            <div className="p-4 bg-white">
              <h3 className="font-medium text-gray-800">Portfolio Asset Allocation</h3>
              <p className="text-sm text-gray-600 mt-1">
                This pie chart shows the distribution of assets in a sample investment portfolio.
                Stocks make up the largest portion at 45%, followed by bonds at 25%.
              </p>
            </div>
          </div>
        </TabsContent>
        
        <TabsContent value="bar" className="mt-4">
          <div className="w-full bg-white rounded-lg shadow-sm border border-gray-200">
            <div className="w-full p-2 sm:p-4 bg-[var(--primary-chart-bg)]">
              <Plot
                data={barChart.data}
                layout={barChart.layout}
                config={plotConfig}
                style={{
                  width: '100%',
                  height: `${config.dynamicHeight}px`,
                  minHeight: '300px',
                }}
                useResizeHandler={true}
                className="w-full"
              />
            </div>
            <div className="p-4 bg-white">
              <h3 className="font-medium text-gray-800">Quarterly Revenue Growth</h3>
              <p className="text-sm text-gray-600 mt-1">
                This bar chart displays quarterly revenue growth over the past five quarters,
                showing a steady increase from $120M in Q1 2023 to $210M in Q1 2024.
              </p>
            </div>
          </div>
        </TabsContent>
        
        <TabsContent value="line" className="mt-4">
          <div className="w-full bg-white rounded-lg shadow-sm border border-gray-200">
            <div className="w-full p-2 sm:p-4 bg-[var(--primary-chart-bg)]">
              <Plot
                data={lineChart.data}
                layout={lineChart.layout}
                config={plotConfig}
                style={{
                  width: '100%',
                  height: `${config.dynamicHeight}px`,
                  minHeight: '300px',
                }}
                useResizeHandler={true}
                className="w-full"
              />
            </div>
            <div className="p-4 bg-white">
              <h3 className="font-medium text-gray-800">Monthly Stock Price Performance</h3>
              <p className="text-sm text-gray-600 mt-1">
                This line chart tracks the monthly stock price performance throughout the year,
                showing an overall upward trend with some fluctuations in March and September.
              </p>
            </div>
          </div>
        </TabsContent>
        
        <TabsContent value="multiline" className="mt-4">
          <div className="w-full bg-white rounded-lg shadow-sm border border-gray-200">
            <div className="w-full p-2 sm:p-4 bg-[var(--primary-chart-bg)]">
              <Plot
                data={multiLineChart.data}
                layout={multiLineChart.layout}
                config={plotConfig}
                style={{
                  width: '100%',
                  height: `${config.dynamicHeight}px`,
                  minHeight: '300px',
                }}
                useResizeHandler={true}
                className="w-full"
              />
            </div>
            <div className="p-4 bg-white">
              <h3 className="font-medium text-gray-800">5-Year Financial Performance</h3>
              <p className="text-sm text-gray-600 mt-1">
                This multi-line chart compares revenue, profit, and expenses over a 5-year period,
                showing consistent growth in all three metrics with revenue growing at the fastest rate.
              </p>
            </div>
          </div>
        </TabsContent>
      </Tabs>
    </div>
  );
};

export default FinancialChartExamples;