#import http
#url="https://api.linode.com/v4/linode/types"
#response1 = http.get(url)
#response2 = json.decode(response1)
response2='''{
    "data": [
        {
            "id": "g6-nanode-1",
            "label": "Nanode 1GB",
            "price": {
                "hourly": 0.0075,
                "monthly": 5.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.009,
                    "monthly": 6.0
                },
                {
                    "id": "br-gru",
                    "hourly": 0.0105,
                    "monthly": 7.0
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.003,
                        "monthly": 2.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.0036,
                            "monthly": 2.4
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.004,
                            "monthly": 2.8
                        }
                    ]
                }
            },
            "memory": 1024,
            "disk": 25600,
            "transfer": 1000,
            "vcpus": 1,
            "gpus": 0,
            "network_out": 1000,
            "class": "nanode",
            "successor": "something"
        },
        {
            "id": "g6-standard-1",
            "label": "Linode 2GB",
            "price": {
                "hourly": 0.018,
                "monthly": 12.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.022,
                    "monthly": 14.4
                },
                {
                    "id": "br-gru",
                    "hourly": 0.025,
                    "monthly": 16.8
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.004,
                        "monthly": 2.5
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.0045,
                            "monthly": 3.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.005,
                            "monthly": 3.5
                        }
                    ]
                }
            },
            "memory": 2048,
            "disk": 51200,
            "transfer": 2000,
            "vcpus": 1,
            "gpus": 0,
            "network_out": 2000,
            "class": "standard",
            "successor": null
        },
        {
            "id": "g6-standard-2",
            "label": "Linode 4GB",
            "price": {
                "hourly": 0.036,
                "monthly": 24.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.043,
                    "monthly": 28.8
                },
                {
                    "id": "br-gru",
                    "hourly": 0.05,
                    "monthly": 33.6
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.008,
                        "monthly": 5.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.009,
                            "monthly": 6.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.01,
                            "monthly": 7.0
                        }
                    ]
                }
            },
            "memory": 4096,
            "disk": 81920,
            "transfer": 4000,
            "vcpus": 2,
            "gpus": 0,
            "network_out": 4000,
            "class": "standard",
            "successor": null
        },
        {
            "id": "g6-standard-4",
            "label": "Linode 8GB",
            "price": {
                "hourly": 0.072,
                "monthly": 48.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.086,
                    "monthly": 57.6
                },
                {
                    "id": "br-gru",
                    "hourly": 0.101,
                    "monthly": 67.2
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.015,
                        "monthly": 10.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.018,
                            "monthly": 12.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.021,
                            "monthly": 14.0
                        }
                    ]
                }
            },
            "memory": 8192,
            "disk": 163840,
            "transfer": 5000,
            "vcpus": 4,
            "gpus": 0,
            "network_out": 5000,
            "class": "standard",
            "successor": null
        },
        {
            "id": "g6-standard-6",
            "label": "Linode 16GB",
            "price": {
                "hourly": 0.144,
                "monthly": 96.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.173,
                    "monthly": 115.2
                },
                {
                    "id": "br-gru",
                    "hourly": 0.202,
                    "monthly": 134.4
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.03,
                        "monthly": 20.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.036,
                            "monthly": 24.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.042,
                            "monthly": 28.0
                        }
                    ]
                }
            },
            "memory": 16384,
            "disk": 327680,
            "transfer": 8000,
            "vcpus": 6,
            "gpus": 0,
            "network_out": 6000,
            "class": "standard",
            "successor": null
        },
        {
            "id": "g6-standard-8",
            "label": "Linode 32GB",
            "price": {
                "hourly": 0.288,
                "monthly": 192.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.346,
                    "monthly": 230.4
                },
                {
                    "id": "br-gru",
                    "hourly": 0.403,
                    "monthly": 268.8
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.06,
                        "monthly": 40.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.072,
                            "monthly": 48.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.084,
                            "monthly": 56.0
                        }
                    ]
                }
            },
            "memory": 32768,
            "disk": 655360,
            "transfer": 16000,
            "vcpus": 8,
            "gpus": 0,
            "network_out": 7000,
            "class": "standard",
            "successor": null
        },
        {
            "id": "g6-standard-16",
            "label": "Linode 64GB",
            "price": {
                "hourly": 0.576,
                "monthly": 384.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.691,
                    "monthly": 460.8
                },
                {
                    "id": "br-gru",
                    "hourly": 0.806,
                    "monthly": 537.6
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.12,
                        "monthly": 80.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.144,
                            "monthly": 96.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.168,
                            "monthly": 112.0
                        }
                    ]
                }
            },
            "memory": 65536,
            "disk": 1310720,
            "transfer": 20000,
            "vcpus": 16,
            "gpus": 0,
            "network_out": 9000,
            "class": "standard",
            "successor": null
        },
        {
            "id": "g6-standard-20",
            "label": "Linode 96GB",
            "price": {
                "hourly": 0.864,
                "monthly": 576.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 1.037,
                    "monthly": 691.2
                },
                {
                    "id": "br-gru",
                    "hourly": 1.21,
                    "monthly": 806.4
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.18,
                        "monthly": 120.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.216,
                            "monthly": 144.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.252,
                            "monthly": 168.0
                        }
                    ]
                }
            },
            "memory": 98304,
            "disk": 1966080,
            "transfer": 20000,
            "vcpus": 20,
            "gpus": 0,
            "network_out": 10000,
            "class": "standard",
            "successor": null
        },
        {
            "id": "g6-standard-24",
            "label": "Linode 128GB",
            "price": {
                "hourly": 1.152,
                "monthly": 768.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 1.382,
                    "monthly": 921.6
                },
                {
                    "id": "br-gru",
                    "hourly": 1.613,
                    "monthly": 1075.2
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.24,
                        "monthly": 160.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.288,
                            "monthly": 192.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.336,
                            "monthly": 224.0
                        }
                    ]
                }
            },
            "memory": 131072,
            "disk": 2621440,
            "transfer": 20000,
            "vcpus": 24,
            "gpus": 0,
            "network_out": 11000,
            "class": "standard",
            "successor": null
        },
        {
            "id": "g6-standard-32",
            "label": "Linode 192GB",
            "price": {
                "hourly": 1.728,
                "monthly": 1152.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 2.074,
                    "monthly": 1382.4
                },
                {
                    "id": "br-gru",
                    "hourly": 2.419,
                    "monthly": 1612.8
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.36,
                        "monthly": 240.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.432,
                            "monthly": 288.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.504,
                            "monthly": 336.0
                        }
                    ]
                }
            },
            "memory": 196608,
            "disk": 3932160,
            "transfer": 20000,
            "vcpus": 32,
            "gpus": 0,
            "network_out": 12000,
            "class": "standard",
            "successor": null
        },
        {
            "id": "g7-highmem-1",
            "label": "Linode 24GB",
            "price": {
                "hourly": 0.09,
                "monthly": 60.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.108,
                    "monthly": 72.0
                },
                {
                    "id": "br-gru",
                    "hourly": 0.126,
                    "monthly": 84.0
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.0075,
                        "monthly": 5.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.009,
                            "monthly": 6.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.0105,
                            "monthly": 7.0
                        }
                    ]
                }
            },
            "memory": 24576,
            "disk": 20480,
            "transfer": 5000,
            "vcpus": 2,
            "gpus": 0,
            "network_out": 5000,
            "class": "highmem",
            "successor": null
        },
        {
            "id": "g7-highmem-2",
            "label": "Linode 48GB",
            "price": {
                "hourly": 0.18,
                "monthly": 120.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.216,
                    "monthly": 144.0
                },
                {
                    "id": "br-gru",
                    "hourly": 0.252,
                    "monthly": 168.0
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.015,
                        "monthly": 10.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.018,
                            "monthly": 12.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.021,
                            "monthly": 14.0
                        }
                    ]
                }
            },
            "memory": 49152,
            "disk": 40960,
            "transfer": 6000,
            "vcpus": 2,
            "gpus": 0,
            "network_out": 6000,
            "class": "highmem",
            "successor": null
        },
        {
            "id": "g7-highmem-4",
            "label": "Linode 90GB",
            "price": {
                "hourly": 0.36,
                "monthly": 240.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.432,
                    "monthly": 288.0
                },
                {
                    "id": "br-gru",
                    "hourly": 0.504,
                    "monthly": 336.0
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.03,
                        "monthly": 20.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.036,
                            "monthly": 24.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.042,
                            "monthly": 28.0
                        }
                    ]
                }
            },
            "memory": 92160,
            "disk": 92160,
            "transfer": 7000,
            "vcpus": 4,
            "gpus": 0,
            "network_out": 7000,
            "class": "highmem",
            "successor": null
        },
        {
            "id": "g7-highmem-8",
            "label": "Linode 150GB",
            "price": {
                "hourly": 0.72,
                "monthly": 480.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.864,
                    "monthly": 576.0
                },
                {
                    "id": "br-gru",
                    "hourly": 1.008,
                    "monthly": 672.0
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.06,
                        "monthly": 40.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.072,
                            "monthly": 48.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.084,
                            "monthly": 56.0
                        }
                    ]
                }
            },
            "memory": 153600,
            "disk": 204800,
            "transfer": 8000,
            "vcpus": 8,
            "gpus": 0,
            "network_out": 8000,
            "class": "highmem",
            "successor": null
        },
        {
            "id": "g7-highmem-16",
            "label": "Linode 300GB",
            "price": {
                "hourly": 1.44,
                "monthly": 960.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 1.728,
                    "monthly": 1152.0
                },
                {
                    "id": "br-gru",
                    "hourly": 2.016,
                    "monthly": 1344.0
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.12,
                        "monthly": 80.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.144,
                            "monthly": 96.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.168,
                            "monthly": 112.0
                        }
                    ]
                }
            },
            "memory": 307200,
            "disk": 348160,
            "transfer": 9000,
            "vcpus": 16,
            "gpus": 0,
            "network_out": 9000,
            "class": "highmem",
            "successor": null
        },
        {
            "id": "g6-dedicated-2",
            "label": "Dedicated 4GB",
            "price": {
                "hourly": 0.054,
                "monthly": 36.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.065,
                    "monthly": 43.2
                },
                {
                    "id": "br-gru",
                    "hourly": 0.076,
                    "monthly": 50.4
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.008,
                        "monthly": 5.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.009,
                            "monthly": 6.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.01,
                            "monthly": 7.0
                        }
                    ]
                }
            },
            "memory": 4096,
            "disk": 81920,
            "transfer": 4000,
            "vcpus": 2,
            "gpus": 0,
            "network_out": 4000,
            "class": "dedicated",
            "successor": null
        },
        {
            "id": "g6-dedicated-4",
            "label": "Dedicated 8GB",
            "price": {
                "hourly": 0.108,
                "monthly": 72.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.13,
                    "monthly": 86.4
                },
                {
                    "id": "br-gru",
                    "hourly": 0.151,
                    "monthly": 100.8
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.015,
                        "monthly": 10.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.018,
                            "monthly": 12.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.021,
                            "monthly": 14.0
                        }
                    ]
                }
            },
            "memory": 8192,
            "disk": 163840,
            "transfer": 5000,
            "vcpus": 4,
            "gpus": 0,
            "network_out": 5000,
            "class": "dedicated",
            "successor": null
        },
        {
            "id": "g6-dedicated-8",
            "label": "Dedicated 16GB",
            "price": {
                "hourly": 0.216,
                "monthly": 144.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.259,
                    "monthly": 172.8
                },
                {
                    "id": "br-gru",
                    "hourly": 0.302,
                    "monthly": 201.6
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.03,
                        "monthly": 20.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.036,
                            "monthly": 24.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.042,
                            "monthly": 28.0
                        }
                    ]
                }
            },
            "memory": 16384,
            "disk": 327680,
            "transfer": 6000,
            "vcpus": 8,
            "gpus": 0,
            "network_out": 6000,
            "class": "dedicated",
            "successor": null
        },
        {
            "id": "g6-dedicated-16",
            "label": "Dedicated 32GB",
            "price": {
                "hourly": 0.432,
                "monthly": 288.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.518,
                    "monthly": 345.6
                },
                {
                    "id": "br-gru",
                    "hourly": 0.605,
                    "monthly": 403.2
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.06,
                        "monthly": 40.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.072,
                            "monthly": 48.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.084,
                            "monthly": 56.0
                        }
                    ]
                }
            },
            "memory": 32768,
            "disk": 655360,
            "transfer": 7000,
            "vcpus": 16,
            "gpus": 0,
            "network_out": 7000,
            "class": "dedicated",
            "successor": null
        },
        {
            "id": "g6-dedicated-32",
            "label": "Dedicated 64GB",
            "price": {
                "hourly": 0.864,
                "monthly": 576.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 1.037,
                    "monthly": 691.2
                },
                {
                    "id": "br-gru",
                    "hourly": 1.21,
                    "monthly": 806.4
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.12,
                        "monthly": 80.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.144,
                            "monthly": 96.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.168,
                            "monthly": 112.0
                        }
                    ]
                }
            },
            "memory": 65536,
            "disk": 1310720,
            "transfer": 8000,
            "vcpus": 32,
            "gpus": 0,
            "network_out": 8000,
            "class": "dedicated",
            "successor": null
        },
        {
            "id": "g6-dedicated-48",
            "label": "Dedicated 96GB",
            "price": {
                "hourly": 1.296,
                "monthly": 864.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 1.555,
                    "monthly": 1036.8
                },
                {
                    "id": "br-gru",
                    "hourly": 1.814,
                    "monthly": 1209.6
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.18,
                        "monthly": 120.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.216,
                            "monthly": 144.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.252,
                            "monthly": 168.0
                        }
                    ]
                }
            },
            "memory": 98304,
            "disk": 1966080,
            "transfer": 9000,
            "vcpus": 48,
            "gpus": 0,
            "network_out": 9000,
            "class": "dedicated",
            "successor": null
        },
        {
            "id": "g6-dedicated-50",
            "label": "Dedicated 128GB",
            "price": {
                "hourly": 1.728,
                "monthly": 1152.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 2.074,
                    "monthly": 1382.4
                },
                {
                    "id": "br-gru",
                    "hourly": 2.419,
                    "monthly": 1612.8
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.24,
                        "monthly": 160.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.288,
                            "monthly": 192.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.336,
                            "monthly": 224.0
                        }
                    ]
                }
            },
            "memory": 131072,
            "disk": 2560000,
            "transfer": 10000,
            "vcpus": 50,
            "gpus": 0,
            "network_out": 10000,
            "class": "dedicated",
            "successor": null
        },
        {
            "id": "g6-dedicated-56",
            "label": "Dedicated 256GB",
            "price": {
                "hourly": 3.456,
                "monthly": 2304.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 4.147,
                    "monthly": 2764.8
                },
                {
                    "id": "br-gru",
                    "hourly": 4.838,
                    "monthly": 3225.6
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.3,
                        "monthly": 200.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.36,
                            "monthly": 240.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.42,
                            "monthly": 280.0
                        }
                    ]
                }
            },
            "memory": 262144,
            "disk": 5120000,
            "transfer": 11000,
            "vcpus": 56,
            "gpus": 0,
            "network_out": 11000,
            "class": "dedicated",
            "successor": null
        },
        {
            "id": "g6-dedicated-64",
            "label": "Dedicated 512GB",
            "price": {
                "hourly": 6.912,
                "monthly": 4608.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 8.294,
                    "monthly": 5529.6
                },
                {
                    "id": "br-gru",
                    "hourly": 9.677,
                    "monthly": 6451.2
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.36,
                        "monthly": 240.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.432,
                            "monthly": 288.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.504,
                            "monthly": 336.0
                        }
                    ]
                }
            },
            "memory": 524288,
            "disk": 7372800,
            "transfer": 12000,
            "vcpus": 64,
            "gpus": 0,
            "network_out": 12000,
            "class": "dedicated",
            "successor": null
        },
        {
            "id": "g1-gpu-rtx6000-1",
            "label": "Dedicated 32GB + RTX6000 GPU x1",
            "price": {
                "hourly": 1.5,
                "monthly": 1000.0
            },
            "region_prices": [],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.06,
                        "monthly": 40.0
                    },
                    "region_prices": []
                }
            },
            "memory": 32768,
            "disk": 655360,
            "transfer": 16000,
            "vcpus": 8,
            "gpus": 1,
            "network_out": 10000,
            "class": "gpu",
            "successor": null
        },
        {
            "id": "g1-gpu-rtx6000-2",
            "label": "Dedicated 64GB + RTX6000 GPU x2",
            "price": {
                "hourly": 3.0,
                "monthly": 2000.0
            },
            "region_prices": [],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.12,
                        "monthly": 80.0
                    },
                    "region_prices": []
                }
            },
            "memory": 65536,
            "disk": 1310720,
            "transfer": 20000,
            "vcpus": 16,
            "gpus": 2,
            "network_out": 10000,
            "class": "gpu",
            "successor": null
        },
        {
            "id": "g1-gpu-rtx6000-3",
            "label": "Dedicated 96GB + RTX6000 GPU x3",
            "price": {
                "hourly": 4.5,
                "monthly": 3000.0
            },
            "region_prices": [],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.18,
                        "monthly": 120.0
                    },
                    "region_prices": []
                }
            },
            "memory": 98304,
            "disk": 1966080,
            "transfer": 20000,
            "vcpus": 20,
            "gpus": 3,
            "network_out": 10000,
            "class": "gpu",
            "successor": null
        },
        {
            "id": "g1-gpu-rtx6000-4",
            "label": "Dedicated 128GB + RTX6000 GPU x4",
            "price": {
                "hourly": 6.0,
                "monthly": 4000.0
            },
            "region_prices": [],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.24,
                        "monthly": 160.0
                    },
                    "region_prices": []
                }
            },
            "memory": 131072,
            "disk": 2621440,
            "transfer": 20000,
            "vcpus": 24,
            "gpus": 4,
            "network_out": 10000,
            "class": "gpu",
            "successor": null
        },
        {
            "id": "g7-premium-2",
            "label": "Premium 4GB",
            "price": {
                "hourly": 0.0645,
                "monthly": 43.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.078,
                    "monthly": 51.84
                },
                {
                    "id": "br-gru",
                    "hourly": 0.091,
                    "monthly": 60.48
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.008,
                        "monthly": 5.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.009,
                            "monthly": 6.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.01,
                            "monthly": 7.0
                        }
                    ]
                }
            },
            "memory": 4096,
            "disk": 81920,
            "transfer": 4000,
            "vcpus": 2,
            "gpus": 0,
            "network_out": 4000,
            "class": "premium",
            "successor": null
        },
        {
            "id": "g7-premium-4",
            "label": "Premium 8GB",
            "price": {
                "hourly": 0.129,
                "monthly": 86.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.156,
                    "monthly": 103.68
                },
                {
                    "id": "br-gru",
                    "hourly": 0.181,
                    "monthly": 120.96
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.015,
                        "monthly": 10.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.018,
                            "monthly": 12.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.021,
                            "monthly": 14.0
                        }
                    ]
                }
            },
            "memory": 8192,
            "disk": 163840,
            "transfer": 5000,
            "vcpus": 4,
            "gpus": 0,
            "network_out": 5000,
            "class": "premium",
            "successor": null
        },
        {
            "id": "g7-premium-8",
            "label": "Premium 16GB",
            "price": {
                "hourly": 0.2595,
                "monthly": 173.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.311,
                    "monthly": 207.36
                },
                {
                    "id": "br-gru",
                    "hourly": 0.363,
                    "monthly": 241.92
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.03,
                        "monthly": 20.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.036,
                            "monthly": 24.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.042,
                            "monthly": 28.0
                        }
                    ]
                }
            },
            "memory": 16384,
            "disk": 327680,
            "transfer": 6000,
            "vcpus": 8,
            "gpus": 0,
            "network_out": 6000,
            "class": "premium",
            "successor": null
        },
        {
            "id": "g7-premium-16",
            "label": "Premium 32GB",
            "price": {
                "hourly": 0.519,
                "monthly": 346.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 0.622,
                    "monthly": 414.72
                },
                {
                    "id": "br-gru",
                    "hourly": 0.726,
                    "monthly": 483.84
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.06,
                        "monthly": 40.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.072,
                            "monthly": 48.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.084,
                            "monthly": 56.0
                        }
                    ]
                }
            },
            "memory": 32768,
            "disk": 655360,
            "transfer": 7000,
            "vcpus": 16,
            "gpus": 0,
            "network_out": 7000,
            "class": "premium",
            "successor": null
        },
        {
            "id": "g7-premium-32",
            "label": "Premium 64GB",
            "price": {
                "hourly": 1.0365,
                "monthly": 691.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 1.244,
                    "monthly": 829.44
                },
                {
                    "id": "br-gru",
                    "hourly": 1.452,
                    "monthly": 967.68
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.12,
                        "monthly": 80.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.144,
                            "monthly": 96.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.168,
                            "monthly": 112.0
                        }
                    ]
                }
            },
            "memory": 65536,
            "disk": 1310720,
            "transfer": 8000,
            "vcpus": 32,
            "gpus": 0,
            "network_out": 8000,
            "class": "premium",
            "successor": null
        },
        {
            "id": "g7-premium-48",
            "label": "Premium 96GB",
            "price": {
                "hourly": 1.5555,
                "monthly": 1037.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 1.866,
                    "monthly": 1244.16
                },
                {
                    "id": "br-gru",
                    "hourly": 2.177,
                    "monthly": 1451.52
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.18,
                        "monthly": 120.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.216,
                            "monthly": 144.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.252,
                            "monthly": 168.0
                        }
                    ]
                }
            },
            "memory": 98304,
            "disk": 1966080,
            "transfer": 9000,
            "vcpus": 48,
            "gpus": 0,
            "network_out": 9000,
            "class": "premium",
            "successor": null
        },
        {
            "id": "g7-premium-50",
            "label": "Premium 128GB",
            "price": {
                "hourly": 2.073,
                "monthly": 1382.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 2.488,
                    "monthly": 1658.88
                },
                {
                    "id": "br-gru",
                    "hourly": 2.903,
                    "monthly": 1935.36
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.24,
                        "monthly": 160.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.288,
                            "monthly": 192.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.336,
                            "monthly": 224.0
                        }
                    ]
                }
            },
            "memory": 131072,
            "disk": 2560000,
            "transfer": 10000,
            "vcpus": 50,
            "gpus": 0,
            "network_out": 10000,
            "class": "premium",
            "successor": null
        },
        {
            "id": "g7-premium-56",
            "label": "Premium 256GB",
            "price": {
                "hourly": 4.1475,
                "monthly": 2765.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 4.977,
                    "monthly": 3317.76
                },
                {
                    "id": "br-gru",
                    "hourly": 5.806,
                    "monthly": 3870.72
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.3,
                        "monthly": 200.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.36,
                            "monthly": 240.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.42,
                            "monthly": 280.0
                        }
                    ]
                }
            },
            "memory": 262144,
            "disk": 5120000,
            "transfer": 11000,
            "vcpus": 56,
            "gpus": 0,
            "network_out": 11000,
            "class": "premium",
            "successor": null
        },
        {
            "id": "g7-premium-64",
            "label": "Premium 512GB",
            "price": {
                "hourly": 8.295,
                "monthly": 5530.0
            },
            "region_prices": [
                {
                    "id": "id-cgk",
                    "hourly": 9.953,
                    "monthly": 6635.52
                },
                {
                    "id": "br-gru",
                    "hourly": 11.612,
                    "monthly": 7741.44
                }
            ],
            "addons": {
                "backups": {
                    "price": {
                        "hourly": 0.36,
                        "monthly": 240.0
                    },
                    "region_prices": [
                        {
                            "id": "id-cgk",
                            "hourly": 0.432,
                            "monthly": 288.0
                        },
                        {
                            "id": "br-gru",
                            "hourly": 0.504,
                            "monthly": 336.0
                        }
                    ]
                }
            },
            "memory": 524288,
            "disk": 7372800,
            "transfer": 12000,
            "vcpus": 64,
            "gpus": 0,
            "network_out": 12000,
            "class": "premium",
            "successor": null
        }
    ],
    "page": 1,
    "pages": 1,
    "results": 37
}'''

if "successor" in response2:
    print("This line is having null")

#print(response2)
