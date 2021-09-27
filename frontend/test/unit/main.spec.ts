import { shallowMount, Wrapper } from '@vue/test-utils'
import MainComp from '@/pages/index.vue'
type MainCompType = InstanceType<typeof MainComp>;

describe('testing main component', () => {

  /** mock axios to resolve undefined method */
  const mock = jest.fn()
  const axiosMock = {
    mocks: {
      $axios: {
        $get: mock,
        $post: mock
      }
    }
  }

  /** first */
  test('total duration should be zero in string, initially', () => {
    const expected = '0';
    const wrapper: Wrapper<MainCompType & { [key: string]: any }> = shallowMount(MainComp,axiosMock);

    /** expected */
    expect(wrapper.vm.totalDuration).toBe(expected);
  })

  /** second */
  test('simulate button click', () => {
    const payload = {
      id: -1,
      title: 'Testing Task',
      task_date: '2021-10-11',
      start_time: '09:00',
      end_time: '10:00',
      duration: 3600
    }
    const wrapper: Wrapper<MainCompType & { [key: string]: any }> = shallowMount(MainComp,axiosMock);

    /** make sure init dialog is false */
    expect(wrapper.vm.dialog).toBe(false);

    /** simulate button click 'NEW TASK' by calling its function directly */
    wrapper.vm.editItem(payload);

    /** check change */
    expect(wrapper.vm.dialog).toBe(true);
  });
})