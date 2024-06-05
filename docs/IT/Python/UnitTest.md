- 它分为四个部分test fixture、TestCase、test suite、test runner，分别是：
    - Test Fixture：为了开展项测试所需要进行的准备工作，以及所有相关的清理操作；
    - Test Case：一个测试用例是一个独立的测试单元。它检查输入特定的数据时的响应；
    - Test Suite：它用于归档需要一起执行的测试用例；
    - Test Runner：是一个用于执行和输出测试结果的组件

- 注意类名要以Test开头，测试用例的名称要以test开头

- def setUp(self):
    - 前置处理，函数级别，此方法会在调用每个测试函数之前被调用