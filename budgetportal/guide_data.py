category_guides = {
    "adjusted-estimates-of-national-expenditure": "adjusted-estimates-of-national-expenditure",
    "estimates-of-provincial-expenditure": "estimates-of-provincial-expenditure",
    "frameworks-for-conditional-grants-to-provinces": "frameworks-for-conditional-grants",
    "frameworks-for-conditional-grants-to-municipalities": "frameworks-for-conditional-grants",
    "estimates-of-national-expenditure": "estimates-of-national-expenditure",
    "performance-and-expenditure-reviews": "performance-and-expenditure-reviews",
    "in-year-spending": "in-year-spending",
}

guides = {
    "adjusted-estimates-of-national-expenditure": {
        "description": u"This guide relates to the structured adjusted estimates of expenditure data in CSV form the AENE PDF documents on each department page, and the accompanying Excel file with the document\u2019s tables",
        "name": "Adjusted Estimates of National Expenditure",
        "selected_sidebar": "guides",
        "selected_tab": "learning-centre",
        "title": "Adjusted Estimates of National Expenditure (AENE) - vulekamali",
    },
    "estimates-of-national-expenditure": {
        "description": "The Estimates of National Expenditure (ENE) publications describe in detail the planned spending in all national government votes over the three-year medium-term expenditure framework (MTEF) period.",
        "name": "Estimates of National Expenditure",
        "selected_sidebar": "guides",
        "selected_tab": "learning-centre",
        "title": "Estimates of National Expenditure (ENE) - vulekamali",
    },
    "estimates-of-provincial-expenditure": {
        "description": "The Estimates of Provincial Revenue and Expenditure (EPRE) is considered a summary of the departmental Strategic and Performance Plan to a level at which the legislature and the public can engage the provincial departments.",
        "name": "Estimates of Provincial Revenue and Expenditure",
        "selected_sidebar": "guides",
        "selected_tab": "learning-centre",
        "title": "Estimates of Provincial Revenue and Expenditure (EPRE) - vulekamali",
    },
    "frameworks-for-conditional-grants": {
        "description": "Learn where to find the rules for how conditional grants may be spent and how much has been allocated to each municipality and province",
        "name": "Frameworks for Conditional Grants",
        "selected_sidebar": "guides",
        "selected_tab": "learning-centre",
        "title": "Frameworks for Conditional Grants - vulekamali",
    },
    "in-year-spending": {
        "description": "The in-year spending dataset provides monthly totals from the transactions of each department.",
        "name": "In-year spending data",
        "selected_sidebar": "guides",
        "selected_tab": "learning-centre",
        "title": "In-year spending data - vulekamali",
    },
    "index": {
        "description": "South Africa's National and Provincial budget data from National Treasury in partnership with IMALI YETHU.",
        "items": [
            {
                "description": u"This guide relates to the structured adjusted estimates of expenditure data in CSV form the AENE PDF documents on each department page, and the accompanying Excel file with the document\u2019s tables",
                "name": "Adjusted Estimates of National Expenditure",
                "url_path": "/learning-resources/guides/adjusted-estimates-of-national-expenditure",
            },
            {
                "description": "The Estimates of National Expenditure (ENE) publications describe in detail the planned spending in all national government votes over the three-year medium-term expenditure framework (MTEF) period.",
                "name": "Estimates of National Expenditure (ENE)",
                "url_path": "/learning-resources/guides/estimates-of-national-expenditure",
            },
            {
                "description": "The Estimates of Provincial Revenue and Expenditure (EPRE) is considered a summary of the departmental Strategic and Performance Plan to a level at which the legislature and the public can engage the provincial departments.",
                "name": "Estimates of Provincial Revenue and Expenditure",
                "url_path": "/learning-resources/guides/estimates-of-provincial-expenditure",
            },
            {
                "description": "Learn where to find the rules for how conditional grants may be spent and how much has been allocated to each municipality and province",
                "name": "Conditional Grant Frameworks and Allocations",
                "url_path": "/learning-resources/guides/frameworks-for-conditional-grants",
            },
            {
                "description": "The in-year spending dataset provides monthly totals from the transactions of each department.",
                "name": "In-year spending data",
                "url_path": "/learning-resources/guides/in-year-spending",
            },
            {
                "description": "A Performance and Expenditure Review (PER) is a process of reviewing government spending on a particular service, and how effective this spending is.",
                "name": "Performance and Expenditure Reviews (PER)",
                "url_path": "/learning-resources/guides/performance-and-expenditure-reviews",
            },
            {
                "description": "Procurement is the process where government buys goods and services using public money. Government buys goods and services in order to deliver services according to its mandate.",
                "name": "Procurement",
                "url_path": "https://procurement.vulekamali.gov.za/",
            },
        ],
        "selected_sidebar": "guides",
        "selected_tab": "learning-centre",
        "title": "Guides - vulekamali",
    },
    "performance-and-expenditure-reviews": {
        "description": "South Africa's National and Provincial budget data from National Treasury in partnership with IMALI YETHU.",
        "name": "Performance and Expenditure Reviews",
        "selected_sidebar": "guides",
        "selected_tab": "learning-centre",
        "title": "Performance and Expenditure Reviews (PER) - vulekamali",
    },
}

for slug, guide in guides.items():
    guide["slug"] = slug
    guide["url"] = "/guides/%s" % slug
