from behave import *
from pattern import *


@given('I have the components {left caramel} and {left biscuit}')
def have_components(context, biscuit=LeftBiscuit(), caramel=LeftCaramel()):
    context.biscuit = biscuit
    context.caramel = caramel


@when('I request for their similarity')
def request_sim(context):
    context.result = context.caramel.on_the_biscuit(context.biscuit)


@then('I expect the result to be {Left caramel on the Left biscuit. We are the same.}')
def expect_result(context):
    assert context.result == "Left caramel on the Left biscuit. We are the same."


@given('I have the components {left caramel} and {right biscuit}')
def have_components(context, biscuit=RightBiscuit(), caramel=LeftCaramel()):
    context.biscuit = biscuit
    context.caramel = caramel


@when('I request for their difference')
def request_dif(context):
    context.result = context.caramel.on_the_biscuit(context.biscuit)


@then('I expect the result to be {We are not the same.}')
def expect_result(context):
    assert context.result == "We are not the same."


@given('I have the components {right caramel} and {left biscuit}')
def have_components(context, biscuit=LeftBiscuit(), caramel=RightCaramel()):
    context.biscuit = biscuit
    context.caramel = caramel


@when('I request for their difference again')
def request_dif(context):
    context.result = context.caramel.on_the_biscuit(context.biscuit)


@then('I expect the result to be {We are not the same.} again')
def expect_result(context):
    assert context.result == "We are not the same."


@given('I have the {right stick}')
def have_stick(context, stick=RightStick()):
    context.stick = stick


@when('I request for what it is made of')
def request_made_of(context):
    context.result = context.stick.made_of()


@then('I expect the result to be {I\'m Right stick. I\'m made of Right caramel on the Right biscuit. We are the same.}')
def expect_result(context):
    assert context.result == "I\'m Right stick. I\'m made of Right caramel on the Right biscuit. We are the same."


@given('I have the {left stick}')
def have_stick(context, stick=LeftStick()):
    context.stick = stick


@when('I request for what it is made of again')
def request_made_of(context):
    context.result = context.stick.made_of()


@then('I expect the result to be {I\'m Left stick. I\'m made of Left caramel on the Left biscuit. We are the same.}')
def expect_result(context):
    assert context.result == "I\'m Left stick. I\'m made of Left caramel on the Left biscuit. We are the same."
