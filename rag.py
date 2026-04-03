schemes_data = [
    "YSR Rythu Bharosa రైతులకు ఆర్థిక సహాయం అందిస్తుంది",
    "Aarogyasri పేదలకు ఉచిత వైద్యం అందిస్తుంది",
    "YSR Pension Scheme వృద్ధులకు పెన్షన్ ఇస్తుంది"
]

def retrieve_info(query):
    for scheme in schemes_data:
        if any(word in scheme for word in query.split()):
            return scheme
    return "సంబంధిత పథకం సమాచారం లేదు"
