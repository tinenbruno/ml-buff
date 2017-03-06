from ml_buff.models import feature, feature_value

def test_persistence(session):
    testfeature = feature.Feature('test')
    session.add(testfeature)
    session.commit()

    test_feature_value = feature_value.FeatureValue([10], testfeature)
    session.add(test_feature_value)
    session.commit()

    assert test_feature_value.value[0] == 10
    assert test_feature_value.feature.name == 'test'
    assert test_feature_value.id != None