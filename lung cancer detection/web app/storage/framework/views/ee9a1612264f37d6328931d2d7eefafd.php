<?php if (isset($component)) { $__componentOriginal9ac128a9029c0e4701924bd2d73d7f54 = $component; } ?>
<?php $component = App\View\Components\AppLayout::resolve([] + (isset($attributes) && $attributes instanceof Illuminate\View\ComponentAttributeBag ? (array) $attributes->getIterator() : [])); ?>
<?php $component->withName('app-layout'); ?>
<?php if ($component->shouldRender()): ?>
<?php $__env->startComponent($component->resolveView(), $component->data()); ?>
<?php if (isset($attributes) && $attributes instanceof Illuminate\View\ComponentAttributeBag && $constructor = (new ReflectionClass(App\View\Components\AppLayout::class))->getConstructor()): ?>
<?php $attributes = $attributes->except(collect($constructor->getParameters())->map->getName()->all()); ?>
<?php endif; ?>
<?php $component->withAttributes([]); ?>
     <?php $__env->slot('header', null, []); ?> 
        <h2 class="font-semibold text-xl text-gray-800 leading-tight">
            <?php echo e(__('Dashboard')); ?>

        </h2>
     <?php $__env->endSlot(); ?>

    <div class="py-12">
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
            <div class="bg-white overflow-hidden shadow-xl sm:rounded-lg">
                <div class="container">
                    <div class="card">
                        <div class="card-body">

                            <div class="table-responsive">
                                
                                    <table class="table table-striped table-sm w-auto"  id="Tble" > 
                            
                                        <tr> 

                                            <th class='table-coloum-width'>
                                                <img src="<?php echo e(asset('Normal.jpg')); ?>" class="d-block image fluid" style="width: 180px; height: 180px;" alt="Logo">
                                            </th>
                                            <td colspan="3">
                                                <img src="<?php echo e(asset('norm.png')); ?>" class="d-block image fluid" style="width: 35px; height: 35px;" alt="Logo">
                                            </td>
                                            
                                        </tr>
                                        <tr> 
                                            <th class='table-coloum-width'>Cancer</th>
                                            <td colspan="3" style="background-color: rgb(255, 255, 255);">Not Detected</td>
                                        </tr>
                            
                                        <tr>
                                            <th>Cancer Position</th>
                                            <td colspan="3">Normal</td>
                                        </tr>

                                        <tr>
                                            <th>Instructions</th>
                                            <td colspan="3">You don’t have lung cancer..!<br>
                                                            Don’t smoke or quit smoking if you do<br>
                                                            Avoid second hand smoke and other substances that can harm your lungs<br>
                                                            Eat a healthy diet and maintain a weight that’s healthy for you<br>
                                                            Suggest that eating fruits and vegetables (two to six-and-a-half cups per day)
                                            </td>
                                        </tr>
                        
                                    </table> 
                                
                            </div>


                        </div>

                    </div>
                </div>
            </div>
            
        </div>
    </div>
 <?php echo $__env->renderComponent(); ?>
<?php endif; ?>
<?php if (isset($__componentOriginal9ac128a9029c0e4701924bd2d73d7f54)): ?>
<?php $component = $__componentOriginal9ac128a9029c0e4701924bd2d73d7f54; ?>
<?php unset($__componentOriginal9ac128a9029c0e4701924bd2d73d7f54); ?>
<?php endif; ?><?php /**PATH D:\RLC\data Management\Web\LungCancerDetection\resources\views/predict.blade.php ENDPATH**/ ?>