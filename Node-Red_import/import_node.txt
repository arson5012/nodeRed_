[
    {
        "id": "be97806f8233304d",
        "type": "tab",
        "label": "플로우 1",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "a023e1b0b6178353",
        "type": "tab",
        "label": "플로우 2",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "539bd85f.f4a988",
        "type": "ui_tab",
        "name": "Home",
        "icon": "dashboard",
        "disabled": false,
        "hidden": false
    },
    {
        "id": "242a8bc65d0335cd",
        "type": "mqtt-broker",
        "name": "video",
        "broker": "localhost",
        "port": "1883",
        "clientid": "node_mqtt_1",
        "autoConnect": true,
        "usetls": false,
        "protocolVersion": "4",
        "keepalive": "120",
        "cleansession": false,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closeQos": "0",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "willMsg": {},
        "sessionExpiry": ""
    },
    {
        "id": "cc7fb3c0331f0a3a",
        "type": "ui_base",
        "theme": {
            "name": "theme-light",
            "lightTheme": {
                "default": "#0094CE",
                "baseColor": "#0094CE",
                "baseFont": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif",
                "edited": true,
                "reset": false
            },
            "darkTheme": {
                "default": "#097479",
                "baseColor": "#097479",
                "baseFont": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif",
                "edited": false
            },
            "customTheme": {
                "name": "Untitled Theme 1",
                "default": "#4B7930",
                "baseColor": "#4B7930",
                "baseFont": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif"
            },
            "themeState": {
                "base-color": {
                    "default": "#0094CE",
                    "value": "#0094CE",
                    "edited": false
                },
                "page-titlebar-backgroundColor": {
                    "value": "#0094CE",
                    "edited": false
                },
                "page-backgroundColor": {
                    "value": "#fafafa",
                    "edited": false
                },
                "page-sidebar-backgroundColor": {
                    "value": "#ffffff",
                    "edited": false
                },
                "group-textColor": {
                    "value": "#1bbfff",
                    "edited": false
                },
                "group-borderColor": {
                    "value": "#ffffff",
                    "edited": false
                },
                "group-backgroundColor": {
                    "value": "#ffffff",
                    "edited": false
                },
                "widget-textColor": {
                    "value": "#111111",
                    "edited": false
                },
                "widget-backgroundColor": {
                    "value": "#0094ce",
                    "edited": false
                },
                "widget-borderColor": {
                    "value": "#ffffff",
                    "edited": false
                },
                "base-font": {
                    "value": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif"
                }
            },
            "angularTheme": {
                "primary": "indigo",
                "accents": "blue",
                "warn": "red",
                "background": "grey",
                "palette": "light"
            }
        },
        "site": {
            "name": "Node-RED Dashboard",
            "hideToolbar": "false",
            "allowSwipe": "false",
            "lockMenu": "false",
            "allowTempTheme": "true",
            "dateFormat": "DD/MM/YYYY",
            "sizes": {
                "sx": 48,
                "sy": 48,
                "gx": 6,
                "gy": 6,
                "cx": 6,
                "cy": 6,
                "px": 0,
                "py": 0
            }
        }
    },
    {
        "id": "6706af4e93584fab",
        "type": "mqtt-broker",
        "name": "Result",
        "broker": "localhost",
        "port": "1883",
        "clientid": "",
        "autoConnect": true,
        "usetls": false,
        "protocolVersion": "4",
        "keepalive": "60",
        "cleansession": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closeQos": "0",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "willMsg": {},
        "sessionExpiry": ""
    },
    {
        "id": "6e03659b127f2941",
        "type": "ui_group",
        "name": "",
        "tab": "539bd85f.f4a988",
        "order": 2,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "fbd536a.22bf9c8",
        "type": "ui_tab",
        "name": "Home",
        "icon": "dashboard"
    },
    {
        "id": "75eba16c.094f9",
        "type": "mqtt-broker",
        "name": "",
        "broker": "127.0.0.1",
        "port": "1883",
        "clientid": "",
        "usetls": false,
        "compatmode": true,
        "keepalive": "60",
        "cleansession": true,
        "birthTopic": "online",
        "birthQos": "0",
        "birthPayload": "BULB-1/LWT",
        "closeTopic": "",
        "closeQos": "0",
        "closePayload": "",
        "willTopic": "offline",
        "willQos": "0",
        "willPayload": "BULB-1/LWT"
    },
    {
        "id": "e266fa112914a318",
        "type": "mqtt-broker",
        "name": "Chart",
        "broker": "localhost",
        "port": "1883",
        "clientid": "",
        "autoConnect": true,
        "usetls": false,
        "protocolVersion": "4",
        "keepalive": "60",
        "cleansession": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closeQos": "0",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "willMsg": {},
        "sessionExpiry": ""
    },
    {
        "id": "e3671ed6e549b625",
        "type": "ui_group",
        "name": "움직임 차트",
        "tab": "539bd85f.f4a988",
        "order": 3,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "3d9e45e.bcd50ba",
        "type": "ui_group",
        "name": "객체 검출",
        "tab": "539bd85f.f4a988",
        "order": 2,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "e625ce36.34cf3",
        "type": "ui_tab",
        "name": "Widgets",
        "icon": "dashboard",
        "order": 2,
        "disabled": false,
        "hidden": true
    },
    {
        "id": "d9bf7560.df5e58",
        "type": "ui_tab",
        "name": "Test",
        "icon": "dashboard",
        "order": 9,
        "disabled": false,
        "hidden": false
    },
    {
        "id": "2d5c9e7551642fa6",
        "type": "ui_group",
        "name": "Web",
        "tab": "539bd85f.f4a988",
        "order": 4,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "ec36a139.98c918",
        "type": "mqtt in",
        "z": "be97806f8233304d",
        "name": "",
        "topic": "test2",
        "qos": "2",
        "datatype": "auto",
        "broker": "242a8bc65d0335cd",
        "nl": false,
        "rap": false,
        "inputs": 0,
        "x": 190,
        "y": 260,
        "wires": [
            [
                "9e3f128a59f94144"
            ]
        ]
    },
    {
        "id": "f221d617.4c46a",
        "type": "template",
        "z": "be97806f8233304d",
        "name": "Image in",
        "field": "payload",
        "fieldType": "msg",
        "format": "html",
        "syntax": "mustache",
        "template": "<img src=\"data:image/png;base64,{{payload}}\" style=\"width: 224px; height: 224px;\"/>",
        "output": "str",
        "x": 520,
        "y": 260,
        "wires": [
            [
                "8e6b147e17980c02"
            ]
        ]
    },
    {
        "id": "a823447a1db2148b",
        "type": "mqtt in",
        "z": "be97806f8233304d",
        "name": "",
        "topic": "test1",
        "qos": "2",
        "datatype": "auto",
        "broker": "6706af4e93584fab",
        "nl": false,
        "rap": true,
        "rh": 0,
        "inputs": 0,
        "x": 190,
        "y": 340,
        "wires": [
            [
                "c56853b2d83a7675"
            ]
        ]
    },
    {
        "id": "c56853b2d83a7675",
        "type": "ui_text",
        "z": "be97806f8233304d",
        "group": "3d9e45e.bcd50ba",
        "order": 0,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "결과",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "className": "",
        "x": 450,
        "y": 340,
        "wires": []
    },
    {
        "id": "9e3f128a59f94144",
        "type": "base64",
        "z": "be97806f8233304d",
        "name": "",
        "action": "",
        "property": "payload",
        "x": 360,
        "y": 260,
        "wires": [
            [
                "f221d617.4c46a"
            ]
        ]
    },
    {
        "id": "ad8dd1b80a26f5ab",
        "type": "mqtt in",
        "z": "be97806f8233304d",
        "name": "",
        "topic": "gyro",
        "qos": "2",
        "datatype": "auto",
        "broker": "6706af4e93584fab",
        "nl": false,
        "rap": true,
        "rh": 0,
        "inputs": 0,
        "x": 190,
        "y": 400,
        "wires": [
            [
                "3386c586150d19a5"
            ]
        ]
    },
    {
        "id": "341d0e7ccd1eecb4",
        "type": "ui_chart",
        "z": "be97806f8233304d",
        "name": "",
        "group": "e3671ed6e549b625",
        "order": 1,
        "width": "6",
        "height": "6",
        "label": "",
        "chartType": "line",
        "legend": "true",
        "xformat": "HH:mm:ss",
        "interpolate": "linear",
        "nodata": "",
        "dot": false,
        "ymin": "0",
        "ymax": "",
        "removeOlder": 1,
        "removeOlderPoints": "",
        "removeOlderUnit": "3600",
        "cutout": 0,
        "useOneColor": false,
        "useUTC": false,
        "colors": [
            "#1f77b4",
            "#aec7e8",
            "#ff7f0e",
            "#2ca02c",
            "#98df8a",
            "#d62728",
            "#ff9896",
            "#9467bd",
            "#c5b0d5"
        ],
        "outputs": 1,
        "useDifferentColor": false,
        "className": "",
        "x": 370,
        "y": 540,
        "wires": [
            []
        ]
    },
    {
        "id": "50833815ac0982c8",
        "type": "mqtt in",
        "z": "be97806f8233304d",
        "name": "",
        "topic": "chart/x",
        "qos": "2",
        "datatype": "auto",
        "broker": "e266fa112914a318",
        "nl": false,
        "rap": true,
        "rh": 0,
        "inputs": 0,
        "x": 190,
        "y": 500,
        "wires": [
            [
                "341d0e7ccd1eecb4"
            ]
        ]
    },
    {
        "id": "df590afeb3e38ce9",
        "type": "mqtt in",
        "z": "be97806f8233304d",
        "name": "",
        "topic": "chart/y",
        "qos": "2",
        "datatype": "auto",
        "broker": "e266fa112914a318",
        "nl": false,
        "rap": true,
        "rh": 0,
        "inputs": 0,
        "x": 190,
        "y": 540,
        "wires": [
            [
                "341d0e7ccd1eecb4"
            ]
        ]
    },
    {
        "id": "aba9c77ec7f16b3f",
        "type": "mqtt in",
        "z": "be97806f8233304d",
        "name": "",
        "topic": "chart/z",
        "qos": "2",
        "datatype": "auto",
        "broker": "e266fa112914a318",
        "nl": false,
        "rap": true,
        "rh": 0,
        "inputs": 0,
        "x": 190,
        "y": 580,
        "wires": [
            [
                "341d0e7ccd1eecb4"
            ]
        ]
    },
    {
        "id": "3386c586150d19a5",
        "type": "ui_led",
        "z": "be97806f8233304d",
        "order": 3,
        "group": "e3671ed6e549b625",
        "width": 0,
        "height": 0,
        "label": "움직임 감지",
        "labelPlacement": "left",
        "labelAlignment": "left",
        "colorForValue": [
            {
                "color": "#ff0000",
                "value": "Stop",
                "valueType": "str"
            },
            {
                "color": "#008000",
                "value": "Move",
                "valueType": "str"
            }
        ],
        "allowColorForValueInMessage": false,
        "shape": "circle",
        "showGlow": true,
        "name": "",
        "x": 450,
        "y": 400,
        "wires": []
    },
    {
        "id": "142dae9.49d4751",
        "type": "ui_template",
        "z": "be97806f8233304d",
        "group": "3d9e45e.bcd50ba",
        "name": "Dashboard stylesheet",
        "order": 1,
        "width": 0,
        "height": 0,
        "format": "<style>\n/*\nIt is reasnoble to declare the colors as CSS variables\nso they can be easily called by name where needed.\n\nYou can see that in many places the variables are not used. Change it!\n*/\n\n:root {\n  --color-green-primary: rgb(51, 204, 51);\n  --color-green-secondary: rgb(26, 101, 26);\n  --color-red-primary: rgb(255, 0, 0);\n  --color-red-secondary: rgba(153,0,0,1);\n  --color-gray-primary:rgba(40,40,40,1);\n  --color-gray-secondary:rgba(65,65,65,1);\n  --color-text-primary: rgb(230, 226, 209);\n  --color-widget-border: rgb(100, 149, 237);\n}\n\n/*\nAll CSS adjustments are commented out.\nTurn rules on one by one and see the changes.\nDon't use too many elements cos it wil be confusing\nStart with simple elements like text, slider or button\n\nMany of elements like buttons have states, \nthose rules must be found and adjusted also.\n*/\n\n/*\n.masonry-container {\n    position: relative;\n    width: 100%;\n    height:100%;\n    margin: 0 auto;\n    background: rgb(255,0,0);\n    background: linear-gradient(180deg,  var(--color-gray-primary) 0%, var(--color-gray-secondary) 100%);\n}*/\n\n\n\n.nr-dashboard-cardcontainer {\n    \n    \n    width: 300px; \n    \n    /*box-shadow: inset 0px 1px 4px 0px #000000bb;*/\n    border-radius: 15px;\n}\n\n\n\n.nr-dashboard-theme ui-card-panel {\n    background-color: #33333300;\n    color:var(--color-text-primary);\n    width: 315px; \n    \n    \n    border-radius: 15px;\n    \n}\n\n    \n\n\n\nbody.nr-dashboard-theme md-content md-card {\n    background-color: #33333300;\n    /*color: var(--color-text-primary);\n    text-shadow: 4px 2px 4px #00000045;\n    box-shadow: 0 -1px 5px 1px #00000045;*/\n    width: 300px;\n    \n    border-radius: 12px;\n    border: 1px solid var(--color-widget-border);\n}\n\n\n\n.nr-dashboard-theme ui-card-panel p.nr-dashboard-cardtitle {\n    width: 640px; \n    color: black;\n    text-align: center;\n}\n\n\n\n\n.md-button {\n    display: inline-block;\n    position: relative;\n    cursor: pointer;\n    min-height: 36px;\n    min-width: 88px;\n    line-height: 36px;\n    vertical-align: middle;\n    align-items: center;\n    text-align: center;\n    border-radius: 12px;\n    box-sizing: border-box;\n    -webkit-user-select: none;\n    -moz-user-select: none;\n    -ms-user-select: none;\n    user-select: none;\n    outline: none;\n    border: 0;\n    padding: 0 6px;\n    margin: 6px 8px;\n    background: transparent;\n    color:var(--color-text-primary);\n    white-space: nowrap;\n    text-transform: uppercase;\n    font-weight: 500;\n    font-size: 14px;\n    font-style: inherit;\n    font-variant: inherit;\n    font-family: inherit;\n    text-decoration: none;\n    overflow: hidden;\n    transition: box-shadow .4s cubic-bezier(.25,.8,.25,1),background-color .4s cubic-bezier(.25,.8,.25,1);\n}\n\n\n\n/*\n.nr-dashboard-theme .nr-dashboard-button .md-button {\n    background-color: #88888800;\n    text-align: center;\n    color:var(--color-text-primary);\n}/*\n\n\n.nr-dashboard-theme .nr-dashboard-button .md-button:hover {\n    background-color: #88888855;\n}\n\n\n\n/*\nmd-slider .md-thumb {\n    z-index: 1;\n    position: absolute;\n    left: -10px;\n    top: 14px;\n    width: 20px;\n    height: 20px;\n    border-radius: 20px;\n    -webkit-transform: scale(.7);\n    transform: scale(.7);\n    transition: all .4s cubic-bezier(.25,.8,.25,1);\n    box-shadow: 0 0 6px #00000070;\n}\n\n*/\n\n/*\nAdvanced stuff - dynamic change of card CSS\n\nClasses here can be used to make colored stripe at the top of card\nUsage is not in here, but they are added to md-card when needed within another template\n\n.carderr {\n    background: rgb(255,0,0);\n    background: linear-gradient(180deg, var(--color-red-primary) 0px, var(--color-red-secondary) 3px, rgba(80,80,80,1) 4px, rgba(45,45,45,1) 100%);\n}\n.cardok {\n    background: rgb(39,255,0);\n    background: linear-gradient(180deg, var(--color-green-primary) 0px, var(--color-green-secondary) 3px, rgba(70,70,70,1) 4px, rgba(40,40,40,1) 100%);\n}\n*/\n\n\n\n</style>\n",
        "storeOutMessages": true,
        "fwdInMessages": true,
        "resendOnRefresh": false,
        "templateScope": "global",
        "className": "",
        "x": 660,
        "y": 180,
        "wires": [
            []
        ]
    },
    {
        "id": "8e6b147e17980c02",
        "type": "ui_template",
        "z": "be97806f8233304d",
        "group": "3d9e45e.bcd50ba",
        "name": "",
        "order": 1,
        "width": 0,
        "height": 0,
        "format": "<center><div ng-bind-html=\"msg.payload\" style=\"width: 224px; height: 224px;\"></div></center>\n",
        "storeOutMessages": true,
        "fwdInMessages": true,
        "resendOnRefresh": true,
        "templateScope": "local",
        "className": "",
        "x": 700,
        "y": 260,
        "wires": [
            []
        ]
    },
    {
        "id": "84115d7317987d9e",
        "type": "ui_button",
        "z": "be97806f8233304d",
        "name": "",
        "group": "e3671ed6e549b625",
        "order": 1,
        "width": "6",
        "height": "1",
        "passthru": false,
        "label": "Naver Blog",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "className": "",
        "icon": "",
        "payload": "Naver Blog",
        "payloadType": "str",
        "topic": "",
        "topicType": "str",
        "x": 210,
        "y": 640,
        "wires": [
            [
                "a0f197b09d288e98"
            ]
        ]
    },
    {
        "id": "1291d93844741ac3",
        "type": "ui_template",
        "z": "be97806f8233304d",
        "group": "e3671ed6e549b625",
        "name": "window redirect",
        "order": 3,
        "width": 0,
        "height": 0,
        "format": "<script>\n(function(scope) {\n    scope.$watch('msg.payload', function(data) {\n        if (data == \"Naver Blog\") {\n          window.open(\"https://blog.naver.com/arson5012\");\n          //window.location.href = \"https://blog.naver.com/arson5012\", \"blog\";\n        } \n        if (data == \"GitHub\") {\n          window.open(\"https://github.com/arson5012/nodeRed_\");\n          //window.location.href = \"https://github.com/arson5012/nodeRed_\", \"github\";\n        } \n    });\n})(scope);\n</script>",
        "storeOutMessages": false,
        "fwdInMessages": true,
        "resendOnRefresh": false,
        "templateScope": "local",
        "className": "",
        "x": 580,
        "y": 660,
        "wires": [
            [
                "4315418c8c750d69"
            ]
        ]
    },
    {
        "id": "53d99612b4c64123",
        "type": "ui_button",
        "z": "be97806f8233304d",
        "name": "",
        "group": "e3671ed6e549b625",
        "order": 2,
        "width": "6",
        "height": "1",
        "passthru": false,
        "label": "GitHub",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "className": "",
        "icon": "",
        "payload": "GitHub",
        "payloadType": "str",
        "topic": "",
        "topicType": "str",
        "x": 200,
        "y": 680,
        "wires": [
            [
                "a0f197b09d288e98"
            ]
        ]
    },
    {
        "id": "a0f197b09d288e98",
        "type": "trigger",
        "z": "be97806f8233304d",
        "name": "reset msg",
        "op1": "",
        "op2": "empty",
        "op1type": "pay",
        "op2type": "str",
        "duration": "250",
        "extend": false,
        "overrideDelay": false,
        "units": "ms",
        "reset": "",
        "bytopic": "all",
        "topic": "topic",
        "outputs": 1,
        "x": 400,
        "y": 660,
        "wires": [
            [
                "1291d93844741ac3"
            ]
        ]
    },
    {
        "id": "4315418c8c750d69",
        "type": "debug",
        "z": "be97806f8233304d",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 770,
        "y": 660,
        "wires": []
    },
    {
        "id": "1c9124e9.e36edb",
        "type": "inject",
        "z": "a023e1b0b6178353",
        "name": "",
        "repeat": "",
        "crontab": "",
        "once": false,
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "x": 1969,
        "y": 254,
        "wires": [
            []
        ]
    },
    {
        "id": "48a892ea.b7576c",
        "type": "debug",
        "z": "a023e1b0b6178353",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 2365,
        "y": 351,
        "wires": []
    }
]
