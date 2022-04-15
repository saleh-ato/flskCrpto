am5.ready(function() {

// Create root element
// https://www.amcharts.com/docs/v5/getting-started/#Root_element
var root = am5.Root.new("chartdiv");

// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root.setThemes([
  am5themes_Animated.new(root)
]);

// Create chart
// https://www.amcharts.com/docs/v5/charts/radar-chart/
var chart = root.container.children.push(
  am5radar.RadarChart.new(root, {
    panX: false,
    panY: false,
    startAngle: 180,
    endAngle: 360
  })
);

// Create axis and its renderer
// https://www.amcharts.com/docs/v5/charts/radar-chart/gauge-charts/#Axes
var axisRenderer = am5radar.AxisRendererCircular.new(root, {
  innerRadius: -10,
  strokeOpacity: 1,
  strokeWidth: 15,
  strokeGradient: am5.LinearGradient.new(root, {
    rotation: 0,
    stops: [
      { color: am5.color(0x19d228) },
      { color: am5.color(0xf4fb16) },
      { color: am5.color(0xf6d32b) },
      { color: am5.color(0xfb7116) }
    ]
  })
});

var xAxis = chart.xAxes.push(
  am5xy.ValueAxis.new(root, {
    maxDeviation: 0,
    min: -200,
    max: 200,
    strictMinMax: true,
    renderer: axisRenderer
  })
);

cci=CCI(Closes.slice(-20))
document.getElementsByClassName('cci')[0].innerHTML=cci.toFixed(2)
// CCI_signal(cci)
Oscillator_signal(0,100,-100,70,cci,"cci-signal")
// Add clock hand
// https://www.amcharts.com/docs/v5/charts/radar-chart/gauge-charts/#Clock_hands
var axisDataItem = xAxis.makeDataItem({});
axisDataItem.set("value", cci);
//indicator here


var bullet = axisDataItem.set("bullet", am5xy.AxisBullet.new(root, {
  sprite: am5radar.ClockHand.new(root, {
    radius: am5.percent(99)
  })
}));

xAxis.createAxisRange(axisDataItem);

axisDataItem.get("grid").set("visible", false);

// Make stuff animate on load
chart.appear(1000, 100);

////////////////////////////
var root = am5.Root.new("chartdiv2");

// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root.setThemes([
  am5themes_Animated.new(root)
]);

// Create chart
// https://www.amcharts.com/docs/v5/charts/radar-chart/
var chart = root.container.children.push(
  am5radar.RadarChart.new(root, {
    panX: false,
    panY: false,
    startAngle: 180,
    endAngle: 360
  })
);

// Create axis and its renderer
// https://www.amcharts.com/docs/v5/charts/radar-chart/gauge-charts/#Axes
var axisRenderer = am5radar.AxisRendererCircular.new(root, {
  innerRadius: -10,
  strokeOpacity: 1,
  strokeWidth: 15,
  strokeGradient: am5.LinearGradient.new(root, {
    rotation: 0,
    stops: [
      { color: am5.color(0x19d228) },
      { color: am5.color(0xf4fb16) },
      { color: am5.color(0xf6d32b) },
      { color: am5.color(0xfb7116) }
    ]
  })
});

var xAxis = chart.xAxes.push(
  am5xy.ValueAxis.new(root, {
    maxDeviation: 0,
    min: 0,
    max: 100,
    strictMinMax: true,
    renderer: axisRenderer
  })
);

rsi=RSI(Closes.slice(-14))
document.getElementsByClassName('rsi')[0].innerHTML=rsi.toFixed(2)
//RSI_signal(rsi)
Oscillator_signal(55,70,30,62,rsi,"rsi-signal")
// Add clock hand
// https://www.amcharts.com/docs/v5/charts/radar-chart/gauge-charts/#Clock_hands
var axisDataItem = xAxis.makeDataItem({});
axisDataItem.set("value", rsi);
//indicator here


var bullet = axisDataItem.set("bullet", am5xy.AxisBullet.new(root, {
  sprite: am5radar.ClockHand.new(root, {
    radius: am5.percent(99)
  })
}));

xAxis.createAxisRange(axisDataItem);

axisDataItem.get("grid").set("visible", false);

// Make stuff animate on load
chart.appear(1000, 100);
////////////////////////////////////
var root = am5.Root.new("MFI");

// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root.setThemes([
  am5themes_Animated.new(root)
]);

// Create chart
// https://www.amcharts.com/docs/v5/charts/radar-chart/
var chart = root.container.children.push(
  am5radar.RadarChart.new(root, {
    panX: false,
    panY: false,
    startAngle: 180,
    endAngle: 360
  })
);

// Create axis and its renderer
// https://www.amcharts.com/docs/v5/charts/radar-chart/gauge-charts/#Axes
var axisRenderer = am5radar.AxisRendererCircular.new(root, {
  innerRadius: -10,
  strokeOpacity: 1,
  strokeWidth: 15,
  strokeGradient: am5.LinearGradient.new(root, {
    rotation: 0,
    stops: [
      { color: am5.color(0x19d228) },
      { color: am5.color(0xf4fb16) },
      { color: am5.color(0xf6d32b) },
      { color: am5.color(0xfb7116) }
    ]
  })
});

var xAxis = chart.xAxes.push(
  am5xy.ValueAxis.new(root, {
    maxDeviation: 0,
    min: -100,
    max: 100,
    strictMinMax: true,
    renderer: axisRenderer
  })
);

mfi=MFI(Closes.slice(-14),Volumes.slice(-14))
document.getElementsByClassName('mfi')[0].innerHTML=mfi.toFixed(2)
Oscillator_signal(55,80,20,70,mfi,"mfi-signal")
// Add clock hand
// https://www.amcharts.com/docs/v5/charts/radar-chart/gauge-charts/#Clock_hands
var axisDataItem = xAxis.makeDataItem({});
axisDataItem.set("value", mfi);
//indicator here


var bullet = axisDataItem.set("bullet", am5xy.AxisBullet.new(root, {
  sprite: am5radar.ClockHand.new(root, {
    radius: am5.percent(99)
  })
}));

xAxis.createAxisRange(axisDataItem);

axisDataItem.get("grid").set("visible", false);

// Make stuff animate on load
chart.appear(1000, 100);


}); // end am5.ready()

MA_9_data=[]
bollinger_bands={
    'upper':[],
    'lower':[]
}
for(let index=9;index<Closes.length;index++){
   MA_9_data.push(MA(Closes.slice(index-9,index)))
}
for(let index=20;index<Closes.length;index++){
    temp=BollingerBands(Closes.slice(index-20,index))
    bollinger_bands['upper'].push(temp[0])
    bollinger_bands['lower'].push(temp[1])
}
biggerSingal(parseFloat(MA_9_data.slice(-1)),parseFloat(Closes.slice(-1)),"ma9-signal")
BollingerSignal(parseFloat(bollinger_bands["lower"].slice(-1)),parseFloat(bollinger_bands["upper"].slice(-1)),parseFloat(Closes.slice(-1)))
const DATA_COUNT = 12;
const labels = [];
for (let i = 0; i < DATA_COUNT; ++i) {
  labels.push(i.toString());
}
const data = {
  labels: labels,
  datasets: [
    {
      label: 'Closes',
      data: Closes,
      borderColor: 'rgb(255,0,0)',
    }, {
      label: '9-Hour-MA',
      data: MA_9_data,
      borderColor: 'rgb(0,255,0)',
    }, {
        label: 'Bollinger Upper Band',
        data: bollinger_bands['upper'],
        borderColor: 'rgb(171, 215, 235)',
      },
      {
        label: 'Bollinger Lower Band',
        data: bollinger_bands['lower'],
        borderColor: 'rgb(171, 215, 235)',
      }
  ]
};
/*const ctx = document.getElementById('MA-chart').getContext('2d');
const config = {
    type: 'line',
    data: data,
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Chart.js Line Chart - Cubic interpolation mode'
        },
      },
      interaction: {
        intersect: false,
      },
      scales: {
        x: {
          display: true,
          title: {
            display: true
          }
        },
        y: {
          display: true,
          title: {
            display: true,
            text: 'Value',
                beginAtZero: false
          },
          ticks: {
            stepSize:1000, beginAtZero:false
        }
        },
    }
    },
  };
const myChart = new Chart(ctx,config);*/
am5.ready(function() {
    var root = am5.Root.new("price-chart");
    // Set themes
    // https://www.amcharts.com/docs/v5/concepts/themes/ 
    root.setThemes([
      am5themes_Animated.new(root)
    ]);
    // Create chart
    // https://www.amcharts.com/docs/v5/charts/xy-chart/
    var chart = root.container.children.push(am5xy.XYChart.new(root, {
      panX: true,
      panY: true,
      wheelX: "panX",
      wheelY: "zoomX",
      maxTooltipDistance: 0,
      pinchZoomX:true
    }));
    var xAxis = chart.xAxes.push(am5xy.DateAxis.new(root, {
      maxDeviation: 0.2,
      baseInterval: {
        timeUnit: "hour",
        count: 1
      },
      renderer: am5xy.AxisRendererX.new(root, {}),
      tooltip: am5.Tooltip.new(root, {})
    }));
    
    var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root, {
      renderer: am5xy.AxisRendererY.new(root, {})
    }));
      var series = chart.series.push(am5xy.LineSeries.new(root, {
        name: "قیمت",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value",
        valueXField: "date",
        legendValueText: "{valueY}",
        tooltip: am5.Tooltip.new(root, {
          pointerOrientation: "horizontal",
          labelText: "{valueY}"})
    }));
    var data = data_creator(Closes,Times)
    series.data.setAll(data);
    var series = chart.series.push(am5xy.LineSeries.new(root, {
        name: "میانگین متحرک 9 روزه",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value",
        valueXField: "date",
        legendValueText: "{valueY}",
        tooltip: am5.Tooltip.new(root, {
          pointerOrientation: "horizontal",
          labelText: "{valueY}"})
    }));
    var data = data_creator(MA_9_data,Times.slice(9))
    series.data.setAll(data);
    var series = chart.series.push(am5xy.LineSeries.new(root, {
        name: "باند بالایی بولینگر",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value",
        valueXField: "date",
        legendValueText: "{valueY}",
        tooltip: am5.Tooltip.new(root, {
          pointerOrientation: "horizontal",
          labelText: "{valueY}"})
    }));
    var data = data_creator(bollinger_bands['upper'],Times.slice(20))
    series.data.setAll(data);
    var series = chart.series.push(am5xy.LineSeries.new(root, {
        name: "باند پایینی بولینگر",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value",
        valueXField: "date",
        legendValueText: "{valueY}",
        tooltip: am5.Tooltip.new(root, {
          pointerOrientation: "horizontal",
          labelText: "{valueY}"})
    }));
    var data = data_creator(bollinger_bands['lower'],Times.slice(20))
    series.data.setAll(data);
    series.appear();
    
    function data_creator(data,times){
        date=[]
        values = data;
        compact_data=[]
        for(i=0;i<times.length;i++){
        timestamp=new Date(times[i])
        date.push(timestamp.getTime())
        }
        for(i=0;i<times.length;i++){
        compact_data.push({
        date: date[i],
        value: values[i]
        })
        }
        return compact_data;
    }
        // Add cursor
    // https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
    var cursor = chart.set("cursor", am5xy.XYCursor.new(root, {
      behavior: "none"
    }));
    cursor.lineY.set("visible", false);
    
    
    // Add scrollbar
    // https://www.amcharts.com/docs/v5/charts/xy-chart/scrollbars/
    chart.set("scrollbarX", am5.Scrollbar.new(root, {
      orientation: "horizontal"
    }));
    
    chart.set("scrollbarY", am5.Scrollbar.new(root, {
      orientation: "vertical"
    }));
    
    
    // Add legend
    // https://www.amcharts.com/docs/v5/charts/xy-chart/legend-xy-series/
    var legend = chart.rightAxesContainer.children.push(am5.Legend.new(root, {
      width: 200,
      paddingLeft: 15,
      height: am5.percent(100)
    }));
    
    // When legend item container is hovered, dim all the series except the hovered one
    legend.itemContainers.template.events.on("pointerover", function(e) {
      var itemContainer = e.target;
    
      // As series list is data of a legend, dataContext is series
      var series = itemContainer.dataItem.dataContext;
    
      chart.series.each(function(chartSeries) {
        if (chartSeries != series) {
          chartSeries.strokes.template.setAll({
            strokeOpacity: 1,
            stroke: am5.color(0x000000)
          });
        } else {
          chartSeries.strokes.template.setAll({
            strokeWidth: 6
          });
        }
      })
    })
    
    // When legend item container is unhovered, make all series as they are
    legend.itemContainers.template.events.on("pointerout", function(e) {
      var itemContainer = e.target;
      var series = itemContainer.dataItem.dataContext;
    
      chart.series.each(function(chartSeries) {
        chartSeries.strokes.template.setAll({
          strokeOpacity: 1,
          strokeWidth: 1,
          stroke: chartSeries.get("fill")
        });
      });
    })
    
    legend.itemContainers.template.set("width", am5.p100);
    legend.valueLabels.template.setAll({
      width: am5.p100,
      textAlign: "right"
    });
    
    // It's is important to set legend data after all the events are set on template, otherwise events won't be copied
    legend.data.setAll(chart.series.values);
    
    
    // Make stuff animate on load
    // https://www.amcharts.com/docs/v5/concepts/animations/
    chart.appear(1000, 100);
    
    //MACD
    var MACDs=[]
    for(let index=26;index<Closes.length;index++){
      MACDs.push(MACD(Closes.slice(index-26,index)))
    }
    MACD_signal(MACDs.slice(-1))
    var root = am5.Root.new("MACD");

root.setThemes([am5themes_Animated.new(root)]);

var chart = root.container.children.push(
  am5xy.XYChart.new(root, {
    wheelY: "zoomX"
  })
);

var data= data_creator(MACDs,Times.slice(26))
// Create Y-axis
var yAxis = chart.yAxes.push(
  am5xy.ValueAxis.new(root, {
    extraTooltipPrecision: 1,
    renderer: am5xy.AxisRendererY.new(root, {
      minGridDistance: 30
    })
  })
);

// Create X-Axis
var xAxis = chart.xAxes.push(
  am5xy.DateAxis.new(root, {
    baseInterval: { timeUnit: "hour", count: 1 },
    renderer: am5xy.AxisRendererX.new(root, {
      minGridDistance: 50,
      cellStartLocation: 0.2,
      cellEndLocation: 0.8
    })
  })
);

// Create series
var series = chart.series.push(
  am5xy.SmoothedXLineSeries.new(root, {
    xAxis: xAxis,
    yAxis: yAxis,
    valueYField: "value",
    valueXField: "date",
    tooltip: am5.Tooltip.new(root, {
      labelText:"{valueX.formatDate()}: {valueY}",
      pointerOrientation:"horizontal"
    })
  })
);

series.strokes.template.setAll({
  strokeWidth: 3
});

series.fills.template.setAll({
  fillOpacity: 0.5,
  visible: true
});


series.data.setAll(data);

var rangeDataItem = yAxis.makeDataItem({
  value: -1000,
  endValue: 0
});

var range = series.createAxisRange(rangeDataItem);

range.strokes.template.setAll({
  stroke: am5.color(0xff621f),
  strokeWidth: 3
});

range.fills.template.setAll({
  fill: am5.color(0xff621f),
  fillOpacity: 0.5,
  visible: true
});


// Add cursor
chart.set(
  "cursor",
  am5xy.XYCursor.new(root, {
    behavior: "zoomX",
    xAxis: xAxis
  })
);

xAxis.set(
  "tooltip",
  am5.Tooltip.new(root, {
    themeTags: ["axis"]
  })
);

yAxis.set(
  "tooltip",
  am5.Tooltip.new(root, {
    themeTags: ["axis"]
  })
);
//////////////////-----------DMI----------------//////////////
var DMIs={
  'PDI':[],
  'NDI':[]
}
for(let index=14;index<Closes.length;index++){
  temp=DMI(Highs.slice(index-14,index),Lows.slice(index-14,index),Closes.slice(index-14,index))
  DMIs['PDI'].push(temp[0])
  DMIs['NDI'].push(temp[1])
}
biggerSingal(parseFloat(DMIs['NDI'].slice(-1)),parseFloat(DMIs['PDI'].slice(-1)),"dmi-signal")

var root = am5.Root.new("DMI");
    root.setThemes([
      am5themes_Animated.new(root)
    ]);
    var chart = root.container.children.push(am5xy.XYChart.new(root, {
      panX: true,
      panY: true,
      wheelX: "panX",
      wheelY: "zoomX",
      maxTooltipDistance: 0,
      pinchZoomX:true
    }));
    var xAxis = chart.xAxes.push(am5xy.DateAxis.new(root, {
      maxDeviation: 0.2,
      baseInterval: {
        timeUnit: "hour",
        count: 1
      },
      renderer: am5xy.AxisRendererX.new(root, {}),
      tooltip: am5.Tooltip.new(root, {})
    }));
    
    var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root, {
      renderer: am5xy.AxisRendererY.new(root, {})
    }));
      var series = chart.series.push(am5xy.LineSeries.new(root, {
        name: "DM+",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value",
        valueXField: "date",
        legendValueText: "{valueY}",
        tooltip: am5.Tooltip.new(root, {
          pointerOrientation: "horizontal",
          labelText: "{valueY}"})
    }));
    var data = data_creator(DMIs['PDI'],Times.slice(14))
    series.data.setAll(data);
    var series = chart.series.push(am5xy.LineSeries.new(root, {
        name: "DM-",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value",
        valueXField: "date",
        legendValueText: "{valueY}",
        tooltip: am5.Tooltip.new(root, {
          pointerOrientation: "horizontal",
          labelText: "{valueY}"})
    }));
    var data = data_creator(DMIs['NDI'],Times.slice(14))
    series.data.setAll(data);
    series.appear();
    
    // Add cursor
    // https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
    var cursor = chart.set("cursor", am5xy.XYCursor.new(root, {
      behavior: "none"
    }));
    cursor.lineY.set("visible", false);
    
    
    // Add scrollbar
    // https://www.amcharts.com/docs/v5/charts/xy-chart/scrollbars/
    chart.set("scrollbarX", am5.Scrollbar.new(root, {
      orientation: "horizontal"
    }));
    
    chart.set("scrollbarY", am5.Scrollbar.new(root, {
      orientation: "vertical"
    }));
    
    
    // Add legend
    // https://www.amcharts.com/docs/v5/charts/xy-chart/legend-xy-series/
    var legend = chart.rightAxesContainer.children.push(am5.Legend.new(root, {
      width: 200,
      paddingLeft: 15,
      height: am5.percent(100)
    }));
    
    // When legend item container is hovered, dim all the series except the hovered one
    legend.itemContainers.template.events.on("pointerover", function(e) {
      var itemContainer = e.target;
    
      // As series list is data of a legend, dataContext is series
      var series = itemContainer.dataItem.dataContext;
    
      chart.series.each(function(chartSeries) {
        if (chartSeries != series) {
          chartSeries.strokes.template.setAll({
            strokeOpacity: 1,
            stroke: am5.color(0x000000)
          });
        } else {
          chartSeries.strokes.template.setAll({
            strokeWidth: 6
          });
        }
      })
    })
    
    // When legend item container is unhovered, make all series as they are
    legend.itemContainers.template.events.on("pointerout", function(e) {
      var itemContainer = e.target;
      var series = itemContainer.dataItem.dataContext;
    
      chart.series.each(function(chartSeries) {
        chartSeries.strokes.template.setAll({
          strokeOpacity: 1,
          strokeWidth: 1,
          stroke: chartSeries.get("fill")
        });
      });
    })
    
    legend.itemContainers.template.set("width", am5.p100);
    legend.valueLabels.template.setAll({
      width: am5.p100,
      textAlign: "right"
    });
    
    // It's is important to set legend data after all the events are set on template, otherwise events won't be copied
    legend.data.setAll(chart.series.values);
    
    
    // Make stuff animate on load
    // https://www.amcharts.com/docs/v5/concepts/animations/
    chart.appear(1000, 100);
    




}); // end am5.ready()