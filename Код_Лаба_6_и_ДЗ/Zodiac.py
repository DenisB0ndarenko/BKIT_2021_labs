from behave import *
from config import *


@given('I have Zodiac signs numbers {\'2\'} and {\'3\'} and I have a relation type {\'Любовь\'}')
def have_signs(context, s1='2', s2='3', rltn='Любовь'):
    context.s1 = s1
    context.s2 = s2
    context.rltn = rltn


@when('I check their compatibility in this relation type')
def check(context):
    context.result = conclusion(context.s1, context.s2, context.rltn)


@then('I expect to get a result True')
def expect_result(context):
    assert context.result


@given('I have Zodiac signs numbers {\'0\'} and {\'1\'} and I have a relation type {\'Работа\'}')
def have_signs(context, s1='0', s2='1', rltn='Работа'):
    context.s1 = s1
    context.s2 = s2
    context.rltn = rltn


@when('I check their compatibility in this relation type again')
def check(context):
    context.result = conclusion(context.s1, context.s2, context.rltn)


@then('I expect to get a result False')
def expect_result(context):
    assert not context.result
